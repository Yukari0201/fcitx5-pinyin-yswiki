from mw2fcitx.tweaks.moegirl import tweaks, tweak_opencc_t2s

exports = {
    "source": {
        "api_path": "https://wiki.biligame.com/ys/api.php",
        "file_path": [
            # "titles.txt",  # use file-based title source for now
            "extras/yuanshen.txt"
        ],
        "kwargs": {
            "output": "titles.txt",
            "api_params": {
                # Results per API request; same as `aplimit` in MediaWiki docs. (optional)
                "aplimit": 200
            }
        }
    },
    "tweaks": tweaks + [tweak_opencc_t2s],
    "converter": {
        "use": "opencc",
        "kwargs": {
            "fixfile": "fixfile.json"
        }
    },
    "generator": [{
        "use": "rime",
        "kwargs": {
            "name": "yuanshen",
            "version": "0.0.1",
            "output": "yuanshen.dict.yaml"
        }
    }, {
        "use": "pinyin",
        "kwargs": {
            "output": "yuanshen.dict"
        }
    }]
}
