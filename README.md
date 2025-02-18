# BERT_IMDB
-----------

The repo contains BERT sentiment classification model fine-tuned IMDB dataset (movie review data) after the BERT model pre-trained on IMDB unsupervised data. Compared with BERT sentiment classification model without pre-training, the BERT model with pre-training on IMDB dataset can be more relevant.

There is a simple web server implement the sentiment prediction of movie review.

# Usage
-------

```bash
git clone https://github.com/WangSteven823/BERT_IMDB.git
```
```bash
cd BERT_IMDB
```
```bash
sudo docker build --no-cache -t dl-pytorch .
```

Only execute a movie review sentiment classification server.

```bash
sudo docker run -d --gpus all --name bert-server -p 8888:8888 -p 5000:5000 -v ../BERT_IMDB/:/BERT_IMDB/ dl-pytorch /bin/bash -c "source activate dl && python server.py" 
```

View and execute code by jupyter notebook.

```bash
sudo docker run -it --gpus all --name bert-model -p 8888:8888 -p 5000:5000 -v ../BERT_IMDB/:/BERT_IMDB/ dl-pytorch
```
```bash
source activate dl 
```
```bash
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root

```

# Folder tree
-------------

```bash
├─dataset
│      test.parquet
│      train.parquet
│      unsupervised.parquet
│      
├─model
│  │  IMDB_BERT.ipynb                            #Bert fine-tuned model.
│  │  IMDB_BERT_PRE_TRAIN.ipynb                  #Bert pre-trained model. 
│  │  
│  ├─bert-finetuned-pretrained-imdb-sentiment    #Bert fine-tuned model.
│  │      config.json
│  │      model.safetensors
│  │      special_tokens_map.json
│  │      tokenizer.json
│  │      tokenizer_config.json
│  │      vocab.txt
│  │      
│  └─bert-pretrained-model-finetuned-imdb        #Bert pre-trained model. 
│          config.json
│          model.safetensors
│          special_tokens_map.json
│          tokenizer.json
│          tokenizer_config.json
│          vocab.txt
│         
├─templates
│      review.html
│        
│  .gitattributes
│  Dockerfile
│  License.txt
│  README.md
│  requirements.txt                                  
│  server.ipynb                                  #Movie review sentiment prediction server.
│  server.py                                     #Movie review sentiment prediction server.
```

# Author
--------
* Steven Wang

# License
---------

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
