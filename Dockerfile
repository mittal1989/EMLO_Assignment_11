FROM python:3.9

WORKDIR /code

RUN pip install \
    torch==1.12.0+cpu \
    torchvision==0.13.0+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html \
    && rm -rf /root/.cache/pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server.py /code/

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]