## ll


## 安装python3.7的anconda环境

```
#切换环境
conda create --name pytorch python=3.7
conda activate pytorch
```

## conda配置国内源

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes

```

## 安装

```
#pytorch与其他依赖库
conda install pytorch=1.3 torchvision jieba scikit-learn nltk matplotlib pandas -c pytorch
```

## 运行 

```shell
python3 demo.py --model readlmodel.pkl
```