FROM continuumio/miniconda3:4.5.4

# docker build -t mfreitas/rnaseq:0.1 .

RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda

RUN conda install -y star multiqc trim-galore subread fastqc

RUN conda install -y picard
