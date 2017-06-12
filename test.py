import midi
# 定义pattern
pattern = midi.Pattern()
# 定义轨道
track = midi.Track()
# 添加轨道到pattern
pattern.append(track)
# 音符开始，并定义位置、音长、音高
on = midi.NoteOnEvent(tick=0, velocity=0, pitch=midi.G_3)
track.append(on)
# 音符结束
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)