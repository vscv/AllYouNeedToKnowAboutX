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
sudo pip3 install albumentations;
