## install_env.sh
* 2021


      sudo apt update;

      # for jupyter output pdf need >100GB dpkg.
      #sudo apt install -y pandoc;
      #sudo apt install -y xelatex;
      #sudo apt install -y texlive-xetex texlive-fonts-recommended texlive-generic-recommended;

      # for TWCC env.
      sudo apt-get install -y libsm6 libxrender1 libxext-dev tree unrar imagemagick graphviz;
      sudo pip3 install visual-logging ipyplot tf-explain tensorflow-addons tensorboard_plugin_profile seaborn scikit-learn scikit-image;
      sudo pip3 install -q "tqdm>=4.36.1";
      sudo pip3 install jupyternotify;
      sudo pip3 install pydot;
      sudo pip3 install albumentations augraphy;
      sudo pip3 install paddlepaddle paddleocr;


* 2023


      # 2020-11-30 created
      # 2021-02-24 updated
      # 2021-12-27 updated
      # 2023-10-12 added psmisc # for 'fuser' the GPU clear!
      # 2023-11-15 added tensorflow-io for decode tiff.
      
      # tricks for TWCC
      # mute the AMP woring
      echo "+ + + export var"
      export TF_ENABLE_AUTO_MIXED_PRECISION=0
      # V100 oom with efnetB7 if bs>4, nor sure its help or not.
      export TF_FORCE_GPU_ALLOW_GROWTH=1
      # cache tf hub models
      export TFHUB_CACHE_DIR=~/tfhub_modules_cache #to cache the hub model. /tmp/tfhub_modules
      
      #timer
      date +"%Y-%m-%d %H:%M:%S"
      
      
      #APT
      #echo "+ + + apt update no -qq"
      #sudo apt update;
      echo "+ + + apt update -qq"
      sudo apt update -qq;
      
      # for 'fuser' the GPU clear!
      sudo apt install psmisc -y -qq;
      
      # for jupyter output pdf need >100GB dpkg.
      # sudo apt install -y pandoc;
      # sudo apt install -y xelatex;
      # sudo apt install -y texlive-xetex texlive-fonts-recommended texlive-generic-recommended;
      
      
      # for TWCC env.
      #echo "+ + + apt install no -qq"
      #sudo apt install -y libgl1-mesa-glx;
      #sudo apt install -y libsm6 libxrender1 libxext-dev tree unrar imagemagick graphviz;
      echo "+ + + apt install -qq"
      sudo apt install -y libgl1-mesa-glx -qq;
      sudo apt install -y libsm6 libxrender1 libxext-dev tree unrar imagemagick graphviz -qq;
      
      
      # for maskrcnn
      sudo apt-get -y install protobuf-compiler -qq; #for maskrcnn/tf od api
      sudo pip3 install -q git+https://github.com/NVIDIA/dllogger.git
      
      
      # PIP
      echo "+ + + pip install -q 1"
      sudo pip3 install -q visual-logging ipyplot tf-explain tensorflow-addons tensorboard_plugin_profile seaborn scikit-learn scikit-image;
      echo "+ + + pip install -q 2"
      sudo pip3 install -q "tqdm>=4.36.1";
      sudo pip3 install -q jupyternotify;
      sudo pip3 install -q pydot;
      echo "+ + + pip install -q 3"
      sudo pip3 install -q albumentations;
      sudo pip3 install -q pytictoc;
      sudo pip3 install -q pycocotools;
      sudo pip3 install -q pytesseract;
      sudo pip install -q tensorflow-io;
      
      
      # for turn off warning of "TF_ENABLE_AUTO_MIXED_PRECISION has no effect."
      # export TF_ENABLE_AUTO_MIXED_PRECISION=0
      
      
      date +"%Y-%m-%d %H:%M:%S"


##### dpkg: debian package. 
