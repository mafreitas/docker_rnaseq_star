FROM continuumio/miniconda3:4.5.4

# docker build -t mfreitas/rnaseq:0.1 .
COPY environment.yml environment.yml

RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda

RUN conda env update -f environment.yml

## Check for latest link: http://downloads.asperasoft.com/en/downloads/8?list
RUN wget -qO- https://download.asperasoft.com/download/sw/connect/3.8.1/ibm-aspera-connect-3.8.1.161274-linux-g2.12-64.tar.gz | tar xvz \
    && chmod +x ibm-aspera-connect-3.8.1.161274-linux-g2.12-64.sh \
    && ./ibm-aspera-connect-3.8.1.161274-linux-g2.12-64.sh

ENV PATH=$PATH:/root/.aspera/connect/bin/

#RUN conda list
#RUN conda info

# when built use the following from inside the docker container to export the environment file

# conda env export > environment.yml
