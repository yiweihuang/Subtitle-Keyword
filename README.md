README
===

How to use
--
>put following files into ```video_file/```
>

* v_chapter_video.csv *(chapter-video map file)*
* video_record.csv *(mongoDB raw data file)*
* filter_just_pass.py  *(filter raw data file that just pass)*

run ```python3 filter_just_pass.py``` will generate

* video_record_filtered.csv

>files in source/
>

* run ```python3 to_weeks.py``` will generate files separated to weeks' videos ```to_weeks/...```

* run ```python preprocess_weeks_data.py``` generate files to dir ```to_weeks_preprecessed```

* run ```python3 subtitlePreprocess.py``` generate files to dir ```it_done```

* run ```python3 generateHotKeyword.py``` generate files to dir ```hot_word```
