import gc
import math
import datetime
import sys
from timm import create_model
from fastai.vision.all import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


def predict_attractiveness(path_to_uploaded_image):
    # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]

    set_seed(2999, reproducible=True)

    # dataset path
    dataset_path = Path('./static/dataset/petfinder-pawpularity-score/')

    df_train = pd.read_csv(dataset_path / 'train.csv')

    df_train['path'] = df_train['Id'].map(lambda x: str(dataset_path / 'train' / x) + '.jpg')
    df_train = df_train.drop(columns=['Id'])
    # shuffle dataframe
    df_train = df_train.sample(frac=1).reset_index(drop=True)

    Pawpularity_max = 100

    df_train['norm_score'] = df_train['Pawpularity'] / Pawpularity_max

    # set seed
    seed = 999
    set_seed(seed, reproducible=True)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.use_deterministic_algorithms = True

    # Sturges' rule
    num_bins = int(np.floor(1 + (3.3) * (np.log2(len(df_train)))))

    df_train['bins'] = pd.cut(df_train['norm_score'], bins=num_bins, labels=False)

    N_FOLDS = 7

    df_train['fold'] = -1

    strat_kfold = StratifiedKFold(n_splits=N_FOLDS, random_state=seed, shuffle=True)

    for i, (_, train_index) in enumerate(strat_kfold.split(df_train.index, df_train['bins'])):
        df_train.iloc[train_index, -1] = i

    df_train['fold'] = df_train['fold'].astype('int')

    def rmse(input_, target):
        res = torch.sqrt(F.mse_loss(Pawpularity_max * F.sigmoid(input_.flatten()), Pawpularity_max * target))
        return res

    fraction = 0.1  # val data fraction
    valid_col = 'is_valid'
    fn_col = "path"
    label_col = 'norm_score'
    batch_size = 8
    num_workers = 8  # for GPU parallel computing
    item_tfms = 224
    batch_tfms = setup_aug_tfms([Brightness(), Contrast(), Hue(), Saturation()])

    # batch_tfms = setup_aug_tfms([Rotate(), Zoom(), Brightness(), Contrast()])

    def get_data(fold):
        df_train_f = df_train.copy()
        # add is_valid for validation fold
        df_train_f['is_valid'] = (df_train_f['fold'] == fold)
        dls = ImageDataLoaders.from_df(
            df_train_f,  # pass in train DataFrame
            valid_pct=fraction,  # train-validation random split
            valid_col=valid_col,
            seed=seed,  # seed
            fn_col=fn_col,  # filename/path is in the second column of the DataFrame
            label_col=label_col,  # label is in the first column of the DataFrame
            y_block=RegressionBlock,  # The type of target
            bs=batch_size,  # pass in batch size
            num_workers=num_workers,
            item_tfms=Resize(224),  # pass in item_tfms
            batch_tfms=batch_tfms  # pass in batch_tfms
        )
        return dls

    # valid Kfolder size
    the_data = get_data(0)
    assert (len(the_data.train) + len(the_data.valid)) == (len(df_train) // batch_size)

    def get_learner(fold_num):
        data = get_data(fold_num)
        model = create_model('swin_large_patch4_window7_224', pretrained=True, num_classes=data.c)
        learn = Learner(data,
                        model,
                        loss_func=BCEWithLogitsLossFlat(),
                        metrics=rmse,
                        path="./static").to_fp16()
        return learn

    df_test = pd.read_csv(dataset_path / 'test.csv')

    df_test['Pawpularity'] = [1] * len(df_test)
    df_test['path'] = df_test['Id'].map(lambda x: str(dataset_path / 'test' / x) + '.jpg')
    df_test = df_test.drop(columns=['Id'])
    df_test['norm_score'] = df_test['Pawpularity'] / 100

    # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
    image_path = Path(path_to_uploaded_image)
    row = {"Subject Focus": 0,
           "Eyes": 0,
           "Face": 0,
           "Near": 0,
           "Action": 0,
           "Accessory": 0,
           "Group": 0,
           "Collage": 0,
           "Human": 0,
           "Occlusion": 0,
           "Info": 0,
           "Blur": 0,
           "Pawpularity": 0,
           "path": image_path,
           "norm_score": 0}

    df_new_image = pd.DataFrame([row], columns=df_test.columns)

    all_preds = []

    for i in range(N_FOLDS):

        print(f'Fold {i} results')

        learn = get_learner(fold_num=i)

        if (i == 0):
            models_path = Path('model_fold_0')
            learn = learn.load(models_path)
        elif (i == 1):
            models_path = Path('model_fold_1')
            learn = learn.load(models_path)
        elif (i == 2):
            models_path = Path('model_fold_2')
            learn = learn.load(models_path)
        elif (i == 3):
            models_path = Path('model_fold_3')
            learn = learn.load(models_path)
        elif (i == 4):
            models_path = Path('model_fold_4')
            learn = learn.load(models_path)
        elif (i == 5):
            models_path = Path('model_fold_5')
            learn = learn.load(models_path)
        elif (i == 6):
            models_path = Path('model_fold_6')
            learn = learn.load(models_path)

        dls = ImageDataLoaders.from_df(df_train,  # pass in train DataFrame
                                        valid_pct=fraction,
                                        seed=seed,  # seed
                                        fn_col=fn_col,  # filename/path is in the second column of the DataFrame
                                        label_col=label_col,  # label is in the first column of the DataFrame
                                        y_block=RegressionBlock,  # The type of target
                                        bs=batch_size,  # pass in batch size
                                        num_workers=num_workers,
                                        item_tfms=Resize(224),  # pass in item_tfms
                                        batch_tfms=setup_aug_tfms(batch_tfms)
                                        )

        test_dl = dls.test_dl(df_new_image)

        preds, _ = learn.tta(dl=test_dl, n=5, beta=0)
        print("preds = ", preds)

        all_preds.extend(preds)

        learn = learn.to_fp32()

        now = datetime.datetime.now()

        del learn, dls, test_dl
        torch.cuda.empty_cache()
        gc.collect()

    preds = np.mean(np.stack(all_preds), axis=0)
    preds = np.squeeze(preds)
    preds = float(preds) * 100  # множимо на 100, щоб бути у межах [0, 100]

    del df_train, df_test, df_new_image

    return preds

# # приклад запуску функції (для тестування)
# result = predict_pawpularity('./static/dataset/petfinder-pawpularity-score/train/0a0da090aa9f0342444a7df4dc250c66.jpg')
