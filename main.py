import os, glob, time, re
import concurrent.futures
import threading
import multiprocessing
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def search_text(texts):
    is_contain = {}
    files = os.listdir('data')
    print('first....', is_contain)
    for file_name in files:
        print('second....', is_contain)
        file_path = 'data/' + file_name
        with open(file_path, 'r') as f:
            file_content = f.read()
            is_found= re.search(texts, file_content)
            # if texts in file_content:
            if is_found:
                is_contain[texts]= file_name, is_found.start(), is_found.end()
                print(is_found.start(), is_found.end())
            else:
                print('Text is not present in ', file_name)
    print('is contain is.....', is_contain)
    return is_contain


def multi_processing(texts):
    texts = re.split(',+', texts)

    with concurrent.futures.ThreadPoolExecutor() as exe:
        doc_list = {}

        results = exe.map(search_text, texts)

        for res in results:
            print('resss.....', type(res))
            doc_list.update(res)
    return doc_list


@app.route('/text_clean', methods=['GET', 'POST'])
def text_clean():
    search_text = request.form.get('fname')

    results = multi_processing(search_text)

    return render_template('index.html', total_docs=results.items())


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    uploaded_file = request.files['myfile']
    uploaded_file.save(os.path.join('data', uploaded_file.filename))
    # response= s3_bucket(uploaded_file.filename)

    return render_template('index.html', filename_= uploaded_file.filename)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
