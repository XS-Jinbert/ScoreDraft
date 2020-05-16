# -*- coding = utf-8 -*-

import python_test.ScoreDraft as ScoreDraft   # 导入库
from python_test.ScoreDraft.Notes import *  # 导入音符

Freqs=[1.0, 9.0/8.0, 81.0/64.0, 4.0/3.0, 3.0/2.0, 27.0/16.0, 243.0/128.0]

def note(octave, freq, duration):
	return (freq*(2.0**(octave-5.0)), duration)

def do(octave=5, duration=48):
	return note(octave,Freqs[0],duration)

def re(octave=5, duration=48):
	return note(octave,Freqs[1],duration)

def mi(octave=5, duration=48):
	return note(octave,Freqs[2],duration)

def fa(octave=5, duration=48):
	return note(octave,Freqs[3],duration)

def so(octave=5, duration=48):
	return note(octave,Freqs[4],duration)

def la(octave=5, duration=48):
	return note(octave,Freqs[5],duration)

def ti(octave=5, duration=48):
	return note(octave,Freqs[6],duration)

def BL(duration=48):
	return (-1.0, duration)

def BK(duration=48):
	return (-1.0, -duration)

FreqsC=Freqs[:]
FreqsF=[f*Freqs[3] for f in Freqs]

Freqs[:]=FreqsF

doc=ScoreDraft.MeteorDocument()		# 创建meteor文件(可视化)
doc.setTempo(129)	# 设置节拍率为每分钟120拍

GePing = ScoreDraft.GePing_UTAU()	# 设置歌手音源——葛平
Piano=ScoreDraft.Piano()			# 设置音源——pinao


track_GePing = doc.newBuf()	 # 葛叔唱歌
track_frist = doc.newBuf()	 # 一轨道
track_second = doc.newBuf()	 # 二轨道

# 和弦
def Chord(elems, duration, delay=0):
	ret=[]
	for elem in elems:
		ret+=[elem[0](elem[1], duration)]
		duration-=delay
		ret+=[BK(duration)]
	ret+=[BL(duration)]
	return ret

# 重复
def Repeat(x, t):
	ret=[]
	for i in range(t):
		ret+=x
	return ret

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

seq_frist = []
seq_second = []
# ======================================================================================================================
# 第1节
seq_frist += [la(5, 24), BL(24), la(4, 48), mi(5, 48), la(4, 24), la(5, 24)]
seq_second += [la(2, 48), la(3, 36), la(3, 12), re(4, 24), mi(4, 24), BL(24), so(2, 24)]
# 第2节
seq_frist += [Repeat(la(5, 24), 2), la(4, 48), mi(5, 48), la(4, 24), la(5, 24)]
seq_second += [BL(24), so(2, 24), la(3, 36), la(3, 12), re(4, 24), mi(4, 24), BL(24), fa(2, 24)]
# 第3节
seq_frist += [Repeat(la(5, 24), 2), la(4, 48), mi(5, 48), la(4, 48)]
seq_second += [BL(24), fa(2, 24), la(3, 36), la(3, 12), so(4, 24), la(4, 24), do(4, 24), re(4, 24)]
# 第4节
seq_GePing=[BL(ScoreDraft.TellDuration(seq_frist))]
seq_GePing += [('o', mi(5, 48), 'la', mi(5, 48), 'mei', do(5, 48), 'mi', la(5, 24), 'si', so(5, 24))]
seq_frist += [mi(5, 48), mi(5, 48), do(5, 48), la(5, 24), so(5, 24)]
seq_second += [mi(3, 48), Repeat(BL(48), 3)]
# ======================================================================================================================
# 第5节
seq_GePing += [('ta', la(5, 24), so(5, 24), la(5, 48),
				BL(24), 'o', so(5, 24), 'mi', mi(5, 24), 'si', la(5, 24))]
seq_frist += [la(5, 24), so(5, 24), la(5, 48), BL(24), so(5, 24), mi(5, 24), la(5, 24)]
seq_second += [la(2, 24), BL(24), mi(4, 36), la(3, 12), so(2, 24), re(4, 24), BL(24), fa(2, 24)]
# 第6节
seq_GePing += [('ta', la(5, 24), so(5, 24), la(5, 48),
				BL(24), 'qi', la(5, 24), 'le', ti(5, 24), 'san', do(5, 24), do(5, 24), )]
seq_frist += [la(5, 24), so(5, 24), la(5, 48), BL(24), la(5, 24), ti(5, 24), do(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 36), do(3, 12), fa(2, 24), mi(2, 24), BL(24), re(2, 24)]
# 第7节
seq_GePing += [('li', ti(5, 24), 'de', la(5, 24), 'hou', do(5, 24), do(5, 24),
				'dou', ti(5, 24), 'shi', la(5, 24), 'zhen', re(5, 24), BL(24))]
seq_frist += [do(5, 24), ti(5, 24), la(5, 24), do(5, 24), do(5, 24), ti(5, 24), la(5, 24), re(5, 24)]
seq_second += [re(2, 24), re(3, 24), la(3, 36), la(2, 12), re(2, 24), mi(2, 24), fa(2, 24), mi(2, 24)]
# 第8节
seq_GePing += [('nan', do(5, 24), BL(24), 'ren', ti(5, 24),
						BL(24), 'hu', la(5, 24), 'ta', ti(5, 24), 'li', ti(5, 24))]
seq_frist += [BL(24), do(5, 24), BL(24), ti(5, 24), BL(24), la(5, 24), ti(5, 24), ti(5, 24)]
seq_second += [BL(24), fa(2, 24), BL(24), so(2, 24), la(2, 24), mi(2, 24), so(2, 24), mi(2, 24)]
# ======================================================================================================================
# 第17节
seq_GePing += [('ta', do(6, 24), 'kan', ti(5, 24), 'dao', la(5, 24), so(5, 24)),
				BL(24), ('ao', so(5, 24), 'pu', mi(5, 24), 'mai', so(5, 24), so(5, 24))]
seq_frist += [do(6, 24), ti(5, 24), la(5, 24), so(5, 24), BL(24), so(5, 24), mi(5, 24), so(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 24), fa(2, 24), fa(2, 24), re(4, 24), mi(3, 24), mi(2, 24)]
# 第18节
seq_GePing += [('gei', la(5, 24), 'lao', ti(5, 12), la(5, 12), la(5, 24),
				BL(24), 'la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), la(5, 24))]
seq_frist += [BL(24), la(5, 24), ti(5, 12), la(5, 12), la(5, 24), BL(24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [BL(24), mi(2, 24), BL(24), la(2, 24), la(2, 24), mi(3, 24), do(3, 24), re(3, 24)]
# 第19节
seq_GePing += [('la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24),
							la(5, 24), 'la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), la(5, 96))]
seq_frist += [la(5, 24), la(5, 24), so(5, 24), la(5, 24), la(5, 24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [re(3, 24), la(3, 24), re(4, 24), mi(3, 24), mi(3, 24), la(3, 24), ti(2, 24), la(2, 24)]
# 第20节
seq_GePing += [BL(96)]
seq_frist += [la(5, 96), do(5, 24), BL(24), do(5, 24), BL(24)]
seq_second += [la(2, 24), la(3, 24), mi(4, 12), so(4, 12), mi(4, 12), la(3, 12), la(2, 24), BL(24), la(2, 24), BL(24)]
# ======================================================================================================================
# 第21节
seq_GePing += [BL(192)]
seq_frist += [BL(48), BL(48), re(5, 24), re(5, 24), BL(24), mi(5, 24)]
seq_second += [so(2, 48), so(3, 36), so(2, 12), so(3, 24), so(2, 24), BL(24), la(2, 24)]
# 第22节
seq_GePing += [BL(48), ('ao', mi(5, 48), 'te', so(5, 48), 'man', mi(5, 24), do(5, 24))]
seq_frist += [BL(48), mi(5, 48), so(5, 48), mi(5, 24), do(5, 24)]
seq_second += [BL(24), la(3, 24), mi(4, 36), mi(3, 12), la(3, 24), so(3, 24), BL(24), fa(3, 24)]
# 第23节
seq_GePing += [('xie', do(5, 24), 'dan', do(5, 24), BL(48),
				'bu', do(5, 24), 'jia', re(5, 24), 'la', mi(5, 24), 'ti', do(5, 24), do(5, 24))]
seq_frist += [do(5, 24), do(5, 24), BL(48), do(5, 24), re(5, 24), mi(5, 24), do(5, 24)]
seq_second += [fa(3, 24), do(3, 24), do(4, 36), mi(3, 12), fa(3, 24), mi(3, 24), BL(24), re(3, 24)]
# 第24节
seq_GePing += [('de', re(5, 24), 'wai', re(5, 24), 'ku', re(5, 24),
				re(5, 24), 'lie',  fa(5, 24), fa(5, 24), 'kai', so(5, 24), so(4, 48))]
seq_frist += [do(5, 24), re(5, 24), re(5, 24), re(5, 24), re(5, 24), fa(5, 24), fa(5, 24), so(5, 24)]
seq_second += [re(3, 24), la(2, 24), la(3, 36), do(3, 12), re(3, 24), mi(3, 24), fa(3, 24), mi(3, 24)]
# ======================================================================================================================
# 第25节
seq_GePing += [('la', fa(5, 24), mi(5, 24)), BL(96)]
seq_frist += [so(4, 48), fa(5, 24), mi(5, 24), BL(24), ti(5, 72)]
seq_second += [BL(24), fa(3, 24), BL(24), so(3, 24), BL(24), so(3, 48), mi(3, 24)]
# 第26节
seq_GePing += [BL(48), ('yi', la(5, 48), 'qi', so(5, 48), 'wan', mi(5, 24), do(5, 24))]
seq_frist += [BL(48), la(5, 48), so(5, 48), mi(5, 24), do(5, 24)]
seq_second += [la(3, 24), BL(24), mi(4, 36), mi(3, 12), la(3, 24), so(3, 24), BL(24), fa(3, 24)]
# 第27节
seq_GePing += [('ma', so(5, 24), la(5, 24), BL(48),
				'gou', do(5, 24), 'yin', re(5, 24), 'ta', mi(5, 24), mi(5, 24))]
seq_frist += [so(5, 24), la(5, 24), BL(48), do(5, 24), re(5, 24), mi(5, 24), mi(5, 24)]
seq_second += [fa(3, 24), do(3, 24), do(4, 36), mi(3, 12), fa(3, 24), mi(3, 24), BL(24), re(3, 24)]
# 第28节
seq_GePing += [('yao', do(5, 24), re(5, 24), 'zhe', re(5, 24), 'na', re(5, 24), re(5, 24),
				'xiong', fa(5, 24), 'bu', fa(5, 24), 'luan', ti(4, 24),ti(4, 48))]
seq_frist += [do(5, 24), re(5, 24), re(5, 24), re(5, 24), re(5, 24), fa(5, 24), fa(5, 24), ti(4, 24)]
seq_second += [re(3, 24), la(2, 24), la(3, 36), do(3, 12), re(3, 24), mi(3, 24), fa(3, 24), mi(3, 24)]
# ======================================================================================================================
# 第29节
seq_GePing += [('dong', so(4, 24), so(4, 24), BL(24),
				'wu', mi(5, 24), 'wen',mi(5, 24), 'ta', mi(5, 24), mi(5, 48))]
seq_frist += [ti(4, 48), so(4, 24), so(4, 24), BL(24), mi(5, 24), mi(5, 24), mi(5, 24)]
seq_second += [mi(3, 24), ti(2, 24), re(3, 24), mi(3, 24), BL(24), mi(3, 24), BL(24), fa(3, 24)]
# 第30节
seq_GePing += [BL(48), ('you', fa(5, 36), 'mei', so(5, 12), 'you', so(5, 24), 'sha', re(5, 24))]
seq_frist += [mi(5, 48), BL(48), fa(5, 36), so(5, 12), so(5, 24), re(5, 24)]
seq_second += [fa(3, 24), la(3, 24), do(4, 36), fa(4, 12), fa(4, 72), do(3, 12)]
# 第31节
seq_GePing += [('ji', ti(5, 48), 'ma', do(6, 36), ti(5, 12)),
			   BL(24), ('o', so(5, 24), 'mei', mi(5, 24), 'you', mi(5, 24))]
seq_frist += [ti(5, 48), do(6, 36), ti(5, 12), BL(24), so(5, 24), mi(5, 24), mi(5, 24)]
seq_second += [fa(3, 48), do(4, 24), fa(4, 24), fa(4, 24), fa(4, 24), do(4, 24), fa(3, 24)]
# 第32节
seq_GePing += [('wo', mi(3, 24), 'mai', so(5, 24), so(5, 24), 'qin', mi(5, 24), so(5, 36),
				'wa', so(5, 12), so(5, 24), 'bei', la(5, 24))]
seq_frist += [mi(3, 24), so(5, 24), so(5, 24), mi(5, 24), so(5, 36), so(5, 12), so(5, 24), la(5, 24)]
seq_second += [mi(3, 24), so(3, 24), ti(3, 24), mi(4, 24), mi(4, 72), ti(2, 24)]
# ======================================================================================================================
# 第33节
seq_GePing += [('dai', mi(5, 24), 'lou', re(5, 48), 'o', do(5, 24), do(5, 48)), BL(24), ('na', mi(5, 24))]
seq_frist += [mi(5, 24), re(5, 48), do(5, 24), do(5, 48), BL(24), mi(5, 24)]
seq_second += [la(2, 24), mi(3, 24), so(3, 24), la(3, 24), la(3, 24), mi(3, 24), la(2, 24), re(3, 24)]
# 第34节
seq_GePing += [('da', mi(5, 24), 'yi', re(5, 48), re(5, 24), re(5, 24),
				'wo', do(5, 24), 'si', re(5, 24), 'da', do(5, 24), re(5, 24))]
seq_frist += [mi(5, 24), re(5, 48), re(5, 24), re(5, 24), do(5, 24), re(5, 24), do(5, 24)]
seq_second += [re(3, 24), fa(3, 24), la(3, 24), re(4, 24), re(4, 72), re(3, 24)]
# 第35节
seq_GePing += [('yi', mi(5, 48), mi(5, 24), mi(5, 48)), BL(48)]
seq_frist += [re(5, 24), mi(5, 48), mi(5, 24), mi(5, 48), BL(24), la(5, 24)]
seq_second += [mi(3, 24), BL(12), ti(2, 12), BL(24), mi(3, 24), mi(3, 24), ti(3, 24), mi(4, 24), mi(2, 24)]
# 第36节
seq_GePing += [('gou', fa(5, 36), 'gou', fa(5, 12), 'lou', fa(5, 24), 'kan', fa(5, 24),
				'bian', mi(5, 24), 'wo', re(5, 24), mi(5, 24), fa(3, 24))]
seq_frist += [fa(5, 36), fa(5, 12), fa(5, 24), fa(5, 24), mi(5, 24), re(5, 24), mi(5, 24), fa(3, 24)]
seq_second += [fa(2, 48), fa(3, 24), do(4, 24), fa(4, 24), do(4, 48), la(2, 24)]
# ======================================================================================================================
# 第37节
seq_GePing += [('gou', re(5, 36), 'gou', re(5, 12), 'lou', re(5, 24), 'kan', re(5, 24),
				'bian', mi(5, 24), 'wo', fa(5, 24), fa(5, 24), fa(5, 24))]
seq_frist += [re(5, 36), re(5, 12), re(5, 24), re(5, 24), mi(5, 24), fa(5, 24), fa(5, 24), fa(5, 24)]
seq_second += [ti(2, 48), fa(3, 24), la(3, 24), la(3, 24), la(3, 24), fa(3, 24), la(2, 24)]
# 第38节
seq_GePing += [('ye', mi(5, 48), 'bu', mi(5, 24), 'ru', re(5, 24), 'ai',
						so(5, 24), 'na', la(5, 24), 'ge', ti(4, 24), 'ku', ti(5, 24))]
seq_frist += [mi(5, 48), mi(5, 24), re(5, 24), so(5, 24), la(5, 24), ti(4, 24), ti(5, 24)]
seq_second += [mi(2, 24), BL(48), re(2, 24), BL(48), re(2, 48)]
# 第39\40节
seq_GePing += [('lao', ti(5, 24), 'tou', so(4, 24), BL(48), 'o', do(6, 48), 'la', la(5, 24), 'mei', so(5, 24))]
seq_frist += [ti(5, 24), so(4, 24), BL(48), do(6, 48), la(5, 24), so(5, 24)]
seq_second += [re(2, 24), mi(2, 24), BL(48), BL(24), mi(3, 24), ti(3, 12), mi(3, 12), BL(12), mi(3, 12)]
# ======================================================================================================================
# 第41节
seq_GePing += [('mi', la(5, 24), 'si', so(5, 24), 'ta', la(5, 48),
				BL(24), 'o', so(5, 24), 'mi', mi(5, 24), 'si', la(5, 24))]
seq_frist += [la(5, 24), so(5, 24), la(5, 48), BL(24), so(5, 24), mi(5, 24), la(5, 24)]
seq_second += [la(2, 24), BL(24), mi(4, 36), la(3, 12), so(2, 24), re(4, 24), BL(24), fa(2, 24)]
# 第42节
seq_GePing += [('ta', la(5, 24), so(5, 24), la(5, 48), BL(24),
				'you',la(5, 24), 'mei', ti(5, 24), 'jia', do(5, 24))]
seq_frist += [la(5, 24), so(5, 24), la(5, 48), BL(24), la(5, 24), ti(5, 24), do(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 36), do(3, 12), fa(2, 24), mi(2, 24), BL(24), re(2, 24)]
# 第43节
seq_GePing += [('la', do(5, 24), 'ni', ti(5, 24), 'la', la(5, 24), 'le', do(5, 24),
				'qing', do(5, 24), ti(5, 24), 'gao', la(5, 24), re(5, 24))]
seq_frist += [do(5, 24), ti(5, 24), la(5, 24), do(5, 24), do(5, 24), ti(5, 24), la(5, 24), re(5, 24)]
seq_second += [re(2, 24), re(3, 24), la(3, 36), la(2, 12), re(2, 24), mi(2, 24), fa(2, 24), mi(2, 24)]
# 第44节
seq_GePing += [BL(24), ('su', do(5, 24), BL(24), 'ta', ti(5, 24), BL(48), 'o', ti(4, 48))]
seq_frist += [BL(24), do(5, 24), BL(24), ti(5, 24), BL(48), ti(4, 48)]
seq_second += [BL(24), fa(2, 24), BL(24), so(2, 24), BL(24), so(2, 48), mi(3, 24)]
# ======================================================================================================================
# 第45节
seq_GePing += [('mi', la(5, 24), 'si', so(5, 24), 'ta', la(5, 48),
				BL(24), 'o', re(5, 24), 'mi', mi(5, 24), 'si', do(5, 24))]
seq_frist += [la(5, 24), so(5, 24), la(5, 48), BL(24), re(5, 24), mi(5, 24), do(5, 24)]
seq_second += [la(2, 24), BL(24), mi(4, 36), la(3, 12), so(2, 24), re(4, 24), BL(24), fa(2, 24)]
# 第46节
seq_GePing += [('ta', do(5, 24), do(5, 24), do(5, 48),
				BL(24), 'a', mi(5, 24), 'na', ti(5, 24), 'ta', re(5, 24), re(5, 24))]
seq_frist += [do(5, 24), do(5, 24), do(5, 48), BL(24), mi(5, 24), ti(5, 24), re(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 36), do(3, 12), fa(2, 24), mi(2, 24), BL(24), re(2, 24)]
# 第47节
seq_GePing += [('nong', ti(5, 24), 'yi', la(5, 24), 'tou', re(5, 24), re(5, 24), 'xin', ti(5, 24), 'tou', la(5, 24), mi(5, 24))]
seq_frist += [re(5, 24), ti(5, 24), la(5, 24), re(5, 24), re(5, 24), ti(5, 24), la(5, 24), mi(5, 24)]
seq_second += [re(2, 24), re(3, 24), la(3, 36), la(2, 12), re(2, 24), mi(2, 24), fa(2, 24), mi(2, 24)]
# 第48节
seq_GePing += [('yi', mi(5, 24), mi(5, 24), BL(24), 'pi', mi(5, 24),
				BL(24), 'wo', ti(5, 24), 'mo', ti(5, 24), ti(5, 24))]
seq_frist += [mi(5, 24), mi(5, 24), BL(24), mi(5, 24), BL(24), ti(5, 24), ti(5, 24), ti(5, 24)]
seq_second += [mi(2, 24), fa(2, 24), so(2, 24), so(2, 24), so(2, 24), so(3, 24), ti(3, 48)]
# ======================================================================================================================
# 第49节
seq_GePing += [('ni', fa(6, 24), 'ni', ti(5, 24), 'mo', la(5, 24), 'wo', ti(5, 24),
				BL(24), 'tu', so(5, 24), 'mo', mi(5, 24), so(5, 24))]
seq_frist += [fa(6, 24), ti(5, 24), la(5, 24), ti(5, 24), BL(24), so(5, 24), mi(5, 24), so(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 24), fa(2, 24), fa(2, 24), re(4, 24), mi(3, 24), mi(2, 24)]
# 第50节
seq_GePing += [BL(48), ('lan', la(5, 24), la(5, 24), BL(24), 'da', do(5, 24), 'yi', ti(5, 24), 'yi', la(5, 24))]
seq_frist += [BL(48), la(5, 24), la(5, 24), BL(24), do(5, 24), ti(5, 24), la(5, 24)]
seq_second += [BL(24), mi(2, 24), BL(24), la(2, 24), la(2, 24), mi(2, 24), so(2, 24), mi(2, 24)]
# 第51节
seq_GePing += [('sheng', fa(5, 24), 'si', fa(5, 24), 'bao', fa(5, 24), 'tai', ti(4, 24),
				BL(24), 'wu', re(5, 24), 'ba', re(5, 24), re(5, 24))]
seq_frist += [fa(5, 24), fa(5, 24), fa(5, 24), ti(4, 24), BL(24), re(5, 24), re(5, 24), re(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 24), so(2, 24), so(2, 24), re(4, 24), so(3, 24), so(2, 24)]
# 第52节
seq_GePing += [BL(24), ('yi', mi(5, 24), 'shang', mi(5, 24), 'tian', mi(5, 24),
				BL(24), 'hu', la(5, 24), 'ta', ti(5, 24), 'li', ti(5, 24))]
seq_frist += [BL(24), mi(5, 24), mi(5, 24), mi(5, 24), BL(24), la(5, 24), ti(5, 24), ti(5, 24)]
seq_second += [BL(24), so(2, 24), BL(24), la(2, 24), la(2, 24), mi(2, 24), so(2, 24), mi(2, 24)]
# ======================================================================================================================
# 第53节
seq_GePing += [('ta', do(6, 24), 'kan', ti(5, 24), 'dao', la(5, 24), so(5, 24)),
				BL(24), ('ao', so(5, 24), 'pu', mi(5, 24), 'mai', so(5, 24), so(5, 24))]
seq_frist += [do(6, 24), ti(5, 24), la(5, 24), so(5, 24), BL(24), so(5, 24), mi(5, 24), so(5, 24)]
seq_second += [fa(2, 24), fa(3, 24), do(4, 24), fa(2, 24), fa(2, 24), re(4, 24), mi(3, 24), mi(2, 24)]
# 第54节
seq_GePing += [('gei', la(5, 24), 'lao', ti(5, 12), la(5, 12), la(5, 24),
				BL(24), 'la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), re(5, 24))]
seq_frist += [BL(24), la(5, 24), ti(5, 12), la(5, 12), la(5, 24), BL(24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [BL(24), mi(2, 24), BL(24), la(2, 24), la(2, 24), mi(3, 24), do(3, 24), re(3, 24)]
# 第55节
seq_GePing += [('la', la(5, 24), 'mie', so(5, 24), 'sou', mi(5, 24), mi(5, 24),
				'la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), la(5, 96))]
seq_frist += [re(5, 24), la(5, 24), so(5, 24), mi(5, 24), mi(5, 24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [re(3, 24), la(3, 24), re(4, 24), mi(3, 24), mi(3, 24), la(3, 24), ti(2, 24), la(2, 24)]
# 第56节
seq_GePing += [BL(24), ('la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), re(5, 24))]
seq_frist += [la(5, 96), BL(24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [la(2, 24), la(3, 24), mi(4, 12), so(4, 12), mi(4, 12), la(3, 12), la(2, 24), mi(3, 24), do(3, 24), re(3, 24)]
# 第57节
seq_GePing += [('la', la(5, 24), 'mie', so(5, 24), 'sou', mi(5, 24), mi(5, 24),
				'la', la(5, 24), 'mie', so(5, 24), 'sou', la(5, 24), la(5, 96))]
seq_frist += [re(5, 24), la(5, 24), so(5, 24), mi(5, 24), mi(5, 24), la(5, 24), so(5, 24), la(5, 24)]
seq_second += [re(3, 24), la(3, 24), re(4, 24), mi(3, 24), mi(3, 24), la(3, 24), ti(2, 24), la(2, 24)]
# 第58节
seq_frist += [la(5, 96)]
seq_second += [la(2, 24), la(3, 24), mi(4, 12), so(4, 12), mi(4, 12), la(3, 12)]

# ======================================================================================================================

doc.playNoteSeq(seq_frist, Piano, track_frist)
doc.playNoteSeq(seq_second, Piano, track_second)

doc.sing(seq_GePing, GePing, track_GePing)

doc.setTrackVolume(track_GePing, 0.6)
doc.setTrackVolume(track_frist, 0.4)
doc.setTrackVolume(track_second, 0.3)

doc.saveToFile('OP.meteor')
doc.meteor()
doc.mixDown('OP.wav')


