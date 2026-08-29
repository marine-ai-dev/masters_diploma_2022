import os
from datetime import datetime

import pandas as pd
from flask import Flask, render_template, request, redirect, flash, url_for, send_file, Response

from database_func import connect_to_mysql_database
from neural_net_func import predict_attractiveness

""" ----------------------------- FLASK PARAMETERS -------------------------------- """
# створюємо додаток через Flask
app = Flask(__name__)
# секретний ключ для додатку
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
# глобальна змінна, що зберігатиме шлях до оброблюваного зображення
image_path = ""
# глобальна змінна для зберігання часу та дати,
# коли було класифіковане зображення для запису у історію БД
my_date_time = ""

# підключаємося до MYSQL
my_db_connection = connect_to_mysql_database()

""" ----------------------------- FLASK FUNCTIONS --------------------------------- """


@app.route("/index.html")
def Home():
    # Якщо є з'єднання із БД - виводимо випадаючий список можливих тварин
    if (my_db_connection):
        my_select = "SELECT * "
        my_from = "FROM PETS "
        my_query = my_select + my_from
        cursor = my_db_connection.cursor()
        cursor.execute(my_query)
        my_records = cursor.fetchall()
        # print("• Total number of rows in DB is: ", cursor.rowcount)
        # for row in my_records:
        #     print(row)
        return render_template('index.html', records=my_records)
    # Якщо БД не підключена - то і випадаючого списку немає
    else:
        return render_template("index.html")



# UPLOAD AN IMAGE
@app.route("/index.html", methods=["POST"])
def upload_image():
    if request.method == "POST":
        # отримуємо завантажену фотографію
        file = request.files["file-image"]
        if (file.filename != ""):

            # Отримуємо результат вибору із випадаючого списку (вибір тварини)
            get_selected_pet = str(request.form.get("select_1"))
            # Отримуємо результат опису тварини із віконця для введення тексту
            get_pet_description = str(request.form.get("text_area_1"))

            # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
            if (get_selected_pet != "" and get_pet_description != ""):
                print("----------------------------------------------------")
                # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
                get_selected_pet = get_selected_pet.split("/")
                # отримуємо pet_id
                get_selected_pet_id = get_selected_pet[0]
                print("• get_selected_pet_id = ", get_selected_pet_id)

                # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
                old_name = file.filename
                # [історичний коментар не вдалось перевірити символ-в-символ під час архівації]
                name, ext = old_name.rsplit('.', 1)

                my_date = str(datetime.now().date())
                my_time = str(datetime.now().time())

                global my_date_time
                my_date_time = my_date + " " + my_time

                my_time = my_time.replace(":", "-")
                my_time = my_time.replace(".", "-")
                result = my_date + "__" + my_time

                new_name = result + "." + ext

                file.filename = new_name

                my_path = './static/uploaded_images/'

                global image_path
                image_path = my_path + file.filename
                print("• image_path = ", image_path)
                print()
                file.save(image_path)

                result = predict_attractiveness(image_path)
                result = round(result, 2)

                if os.path.exists(image_path):
                    os.remove(image_path)
                    print("image was deleted from the folder")

                if (my_db_connection):
                    my_insert = "INSERT INTO CASE_HISTORY (case_datetime, prediction_result, case_info, PETS_pet_id) "
                    my_values = "VALUES( '"\
                                + str(my_date_time) + "', "\
                                + str(result) + ", '"\
                                + str(get_pet_description) + "', "\
                                + str(get_selected_pet_id) + "); "

                    my_query = my_insert + my_values
                    print(my_query)
                    cursor = my_db_connection.cursor()
                    cursor.execute(my_query)
                    my_db_connection.commit()

                    print("THE RECORD WAS SUCCESSFULLY ADDED TO CASE HISTORY. PREDICTION RESULT:", result)
                    flash(str(result), "prediction-result")
                    flash(str(my_date), "prediction-result")
                    flash(str(my_time), "prediction-result")
                    return redirect(url_for('Home', _anchor='anchor-image-window'))
                else:
                    flash("UNABLE TO CONNECT TO DATABASE. PLEASE, TRY LATER!", category="error")
                    return redirect(url_for('Home', _anchor='anchor-image-window'))

            else:
                flash('NOT ALL NOT ALL ITEMS ARE FILLED / SELECTED. TRY AGAIN!', category="error")
                return redirect(url_for('Home', _anchor='anchor-image-window'))

        else:
            print("MEOW-3")
            flash('NO IMAGE WAS SELECTED FOR UPLOADING. PLEASE, CHOOSE AN IMAGE!', category="error")
            return redirect(url_for('Home', _anchor='anchor-image-window'))

# GET DATA FROM DATABASE (CASE HISTORY)
@app.route("/getCaseHistoryCSV", methods=["GET"])
def get_case_history():
    if request.method == "GET":
        if (my_db_connection):

            my_select = "SELECT * "
            my_from = "FROM CASE_HISTORY "
            my_query = my_select + my_from
            cursor = my_db_connection.cursor()
            cursor.execute(my_query)
            my_records = cursor.fetchall()
            my_columns = [i[0] for i in cursor.description]
            print("• Total number of rows in DB is: ", cursor.rowcount)
            print("• Column names: ", my_columns)
            for row in my_records:
                print(row)

            caseHistory = pd.DataFrame(data=my_records, columns=my_columns)

            return Response(
                caseHistory.to_csv(),
                mimetype="text/csv",
                headers={"Content-disposition":
                             "attachment; filename=case-history.csv"})


# GET DATA FROM DATABASE (CASE HISTORY)
@app.route("/getPetsInfoCSV", methods=["GET"])
def get_pets_info():
    if request.method == "GET":
        if (my_db_connection):

            my_select = "SELECT * "
            my_from = "FROM PETS "
            my_query = my_select + my_from
            cursor = my_db_connection.cursor()
            cursor.execute(my_query)
            my_records = cursor.fetchall()
            my_columns = [i[0] for i in cursor.description]
            print("• Total number of rows in DB is: ", cursor.rowcount)
            print("• Column names: ", my_columns)
            for row in my_records:
                print(row)

            petsInfo = pd.DataFrame(data=my_records, columns=my_columns)

            return Response(
                petsInfo.to_csv(),
                mimetype="text/csv",
                headers={"Content-disposition":
                             "attachment; filename=pets-info.csv"})



if __name__ == '__main__':
    app.run(host='0.0.0.0')
