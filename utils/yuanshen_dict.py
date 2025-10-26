from mw2fcitx.tweaks.moegirl import tweaks

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
                "aplimit": "max"
            },
        },
    },
    "tweaks": tweaks,
    "converter": {},
    "generator": [
        {
            "use": "rime",
            "kwargs": {
                "name": "yuanshen",
                "version": "0.0.1",
                "output": "yuanshen.dict.yaml",
            },
        },
        {
            "use": "pinyin",
            "kwargs":
            {"output": "yuanshen.dict"}
        },
    ],
}
