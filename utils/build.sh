#!/bin/bash
set -euo pipefail

pushd /toolkit

pacman -Syu --noconfirm libime uv
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
uv pip install 'mw2fcitx[opencc]'
mw2fcitx -c utils/yuanshen_dict.py

useradd archbuild
chmod -R a+rwx .
export DATE=${1:-$(date +%Y%m%d)} # makepkg.sh also uses the variable
sed -i "s/0.0.1/${DATE}/" utils/yuanshen_dict.py
# https://github.com/docker/for-mac/issues/7331#issuecomment-2198313216
sudo pacman -U --noconfirm https://archive.archlinux.org/packages/f/fakeroot/fakeroot-1.34-1-x86_64.pkg.tar.zst
su archbuild utils/makepkg.sh

cp fcitx5-pinyin-yuanshen* /artifacts
cp ./yuanshen.dict /artifacts
cp ./yuanshen.dict.yaml /artifacts
cp ./titles.txt /artifacts

popd
