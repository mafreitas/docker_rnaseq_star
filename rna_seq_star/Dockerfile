FROM continuumio/miniconda3:4.5.4

# docker build -t mfreitas/rnaseq:0.1 .
COPY environment.yml environment.yml

RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda

RUN conda env update -f environment.yml

RUN conda list
RUN conda info
