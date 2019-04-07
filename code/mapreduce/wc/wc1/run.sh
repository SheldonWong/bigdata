HADOOP_CMD="/home/sheldonwong/env/hadoop-2.6.5/bin/hadoop"
STREAM_JAR_PATH="/home/sheldonwong/env/hadoop-2.6.5/share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar"

INPUT_FILE_PATH_1="/wordcount/a.txt"
OUTPUT_PATH="/bbb"

$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -file ./mapper.py \
    -file ./reducer.py
