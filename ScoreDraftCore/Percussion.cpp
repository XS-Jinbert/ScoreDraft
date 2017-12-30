#include "Percussion.h"
#include "Beat.h"
#include "TrackBuffer.h"
#include <memory.h>
#include <cmath>
#include <vector>

#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif

#ifndef min
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#endif


BeatBuffer::BeatBuffer()
{
	m_sampleNum = 0;
	m_data = 0;
}

BeatBuffer::~BeatBuffer()
{
	delete[] m_data;
}

void BeatBuffer::Allocate()
{
	delete[] m_data;
	m_data = new float[m_sampleNum];
}

class BeatTableItem
{
public:
	int m_duration;
	BeatBuffer m_beatBuffer;
};

#include <cmath>
#include <time.h>
Percussion::Percussion() : m_beatVolume(1.0f)
{
	srand((unsigned)time(NULL));
}

Percussion::~Percussion()
{

}


void Percussion::Silence(unsigned numOfSamples, BeatBuffer* noteBuf)
{
	noteBuf->m_sampleNum = numOfSamples;
	noteBuf->Allocate();
	memset(noteBuf->m_data, 0, sizeof(float)*numOfSamples);
}

void Percussion::GenerateBeatWave(float fNumOfSamples, BeatBuffer* beatBuf, float BufferSampleRate)
{
	Silence((unsigned)ceilf(fNumOfSamples), beatBuf);
}

inline float rand01()
{
	float f = (float)rand() / (float)RAND_MAX;
	if (f < 0.0000001f) f = 0.0000001f;
	if (f > 0.9999999f) f = 0.9999999f;
	return f;
}

void Percussion::PlayBeat(TrackBuffer& buffer, int duration, unsigned tempo)
{
	BeatBuffer beatBuf;

	float fduration = (float)(duration * 60) / (float)(tempo * 48);
	float fNumOfSamples = buffer.Rate()*fduration;

	GenerateBeatWave(fNumOfSamples, &beatBuf, (float)buffer.Rate());
	buffer.WriteBlend(beatBuf.m_sampleNum, beatBuf.m_data, fNumOfSamples);
}

void Percussion::PlaySilence(TrackBuffer& buffer, int duration, unsigned tempo)
{
	float fduration = (float)(duration * 60) / (float)(tempo * 48);
	float fNumOfSamples = buffer.Rate()*fduration;
	buffer.MoveCursor(fNumOfSamples);
}

void Percussion::PlayBackspace(TrackBuffer& buffer, int duration, unsigned tempo)
{
	float fduration = (float)(duration * 60) / (float)(tempo * 48);
	float fNumOfSamples = buffer.Rate()*fduration;
	buffer.MoveCursor(-fNumOfSamples);
	return;
}

void Percussion::PlayBeats(TrackBuffer& buffer, Percussion_deferred* percussionList, const BeatSequence& seq, unsigned tempo)
{
	int i;
	int prog = 0;
	for (i = 0; i<(int)seq.size(); i++)
	{
		int newprog = (i + 1) * 10 / (int)seq.size();
		if (newprog>prog)
		{
			printf("-");
			prog = newprog;
		}
		const Beat& beat = seq[i];
	
		if (beat.m_PercId >= 0)
			percussionList[beat.m_PercId]->PlayBeat(buffer, beat.m_duration, tempo);
		else if (beat.m_duration >= 0)
			PlaySilence(buffer, beat.m_duration, tempo);
		else
			PlayBackspace(buffer, -beat.m_duration, tempo);
	}
	printf("\n");
}


bool Percussion::Tune(const char* cmd)
{
	char command[1024];
	float value;
	sscanf(cmd, "%s %f", &command, &value);
	if (strcmp(command, "volume") == 0)
	{
		m_beatVolume = value;
		return true;
	}
	return false;
}