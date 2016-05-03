#!/usr/bin/env python3

import re
import sys

# 1. 集計は最初にqueueごとに分けて行う。--- yes
#     - runするまではqueueがどこかはわかるはずだが、ノードがどこかわからない
#     - ノードがわからないのでqstatのqueueのところに値が出てこない <= 不便
#     - qalterとかで投入するqueueを後で変えられるってことでしょうね。
#     - でも今の瞬間のtargetを教えてくれたっていいやんね。
#     - それを取得しようと思ったら最悪数万回qstat -j するんですか？
#     - 一時間に一回ぐらいならいいけど、1分に1回とか嫌だな
#     - DBに入れておいて、変化があったものだけ聞きに行くのか...
#     - 終了したjobの判定 -- 簡単か
#
# 
#
#
#
#     そうか、real time application = rethinkdbか...
#
#
# 2. 正解は上記の通りとして、もっと楽に答えに至る方法はないか？
#     - queueごとに待っているjobの情報を出せばいいのかね
#
#     - jobが入らない症状を捉えよ、ってことですか。
#     - 実際にjobを投入してみてどのぐらい時間がかかるのかを見るってことね。
#     - で、その時の様子を記録しておくわけですね。



def main():
    qstat_out_file = sys.argv[1]

    queue_stat(qstat_out_file)
    
    # user_to_state(qstat_out_file)
    # user_to_state_stats()
    # user_to_r_stats()
    # user_to_w_stats()

def queue_stat(qstat_out_file):
    outfile = "user__state.txt"
    fout = open(outfile, "w")

    start_at_p = re.compile(r'\s([0-9]{2}\/[0-9]{2}\/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2})\s')
    queue_p = re.compile(r'[0-9]{2}:[0-9]{2}:[0-9]{2} ([a-z_]+.q)@[a-z0-9]+\s')

    line_no = 0
    for line in open(qstat_out_file):
        line_no = line_no + 1
        if line_no < 3:
            continue
        
        line = line.strip()
        col  = re.split('\s+', line)

        start_at = "00/00/0000 00:00:00"
        m = start_at_p.search(line)
        if m != None:
            start_at = m.group(1)


        queue = "unknown"
        m = queue_p.search(line)
        if m != None:
            queue = m.group(1)

        job_id = col[0] + "(" + start_at + ")"
        fout.write("\t".join( (job_id,col[0],col[2],col[3],col[4],start_at,queue) )+ "\n")

    
    
    
def user_to_state(qstat_out):
    outfile = "user__state.txt"
    fout = open(outfile, "w")
    
    line_no = 0
    for line in open(qstat_out):

        line_no = line_no + 1
        if line_no < 3:
            continue
        
        line = line.strip()
        col  = re.split('\s+', line)
        fout.write(col[3] + "\t" + col[4] + "\n")


def user_to_state_stats():
    freq = {}
    
    for line in open("user__state.txt"):
        line = line.strip()
        col = re.split('\t', line)

        if col[0] in freq:
            freq[col[0]] = freq[col[0]] + 1
        else:
            freq[col[0]] = 1

    for k in freq.keys():
        print(k + "\t" + str(freq[k]))


def user_to_state_stats():
    freq = {}
    
    for line in open("user__state.txt"):
        line = line.strip()
        col = re.split('\t', line)

        if col[0] in freq:
            freq[col[0]] = freq[col[0]] + 1
        else:
            freq[col[0]] = 1

    for k in freq.keys():
        print(k + "\t" + str(freq[k]))

        

if __name__=="__main__":
    main()
