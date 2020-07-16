# Xin, Andrew

# RETURNS a new sound that is the portion of "source" from "start" to "end"
# doesn't alter the original sound     
def clip (source, start, end):
  target = makeEmptySound (end - start, 44100)
  targetIndex = 0
  for sourceIndex in range (start, end):
    sourceValue = getSampleValueAt (source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1
  return target
  
# copies the "source" sound into the "target" sound starting at "start" in "target"
def copy (source, target, start):
  targetIndex = start
  for sourceIndex in range(0, getLength(source)):
    sourceValue = getSampleValueAt (source, sourceIndex)
    setSampleValueAt (target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1


# YOU NEED TO COMPLETE THE FOLLOWING FUNCTION.  DO NOT 
# CHANGE EITHER OF THE FUNCTIONS ABOVE!

# To use the "sentence" function:  run the "setMediaPath()" 
# command in the command area so it will find your recordings.

def sentence():
  s1 = makeSound (getMediaPath ("Sentence1.wav"))
  s2 = makeSound (getMediaPath ("Sentence2.wav"))
  a = getLength(s1)
  b = getLength(s2)
  newS = makeEmptySound (a + b, 44100)
  w1 = clip(s1, 19968, 28160)
  w2 = clip(s2, 28673, 40960)
  w3 = clip(s1, 50665, 62976)
  w4 = clip(s2, 60929, 80064)
  copy(w1, newS, 0)
  copy(w2, newS, getLength(w1))
  copy(w3, newS, getLength(w1) + getLength(w2))
  copy(w4, newS, getLength(w1) + getLength(w2) + getLength(w3))
  return newS
  play(newS)
	
