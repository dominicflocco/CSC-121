"""
This program modifies a given audio file by looping, flipflopping,
fading or echoing the sound.

Authors: Kendall Weinfeld and Dominic Flocco

Time Spent: 4 hours
"""



from csc121.audio import read_wav, write_wav

def loop():
    """Function that loops an audio clip."""
    user_prompt = input("Enter file name: ")
    num_of_repeats = int(input("Enter number of times to repeats: "))
    
    
    samples = read_wav(user_prompt)
    looped = samples * num_of_repeats
    
    write_wav(looped, 'looped.wav') 
    
def flipflop():
    """Function that flipflops an audio clip"""
    user_prompt = input("Enter file name: " )
   
    samples = read_wav(user_prompt)
    half_list = int((len(samples)) / 2)
    flip_flop = []
    first_half = []
    second_half = []
    
    for i in range(half_list):
        first_half.append(samples[i])
        
    for i in range(half_list): 
        second_half.append(samples[i + half_list])
        
    flip_flop = second_half + first_half
    
    write_wav(flip_flop, "flipflopped.wav")
        
def fade():
    """Function that fades out an audio clip"""
    user_prompt = input("Enter file name: ")
    audio = read_wav(user_prompt)
    
    faded = []
    for i in range(len(audio)):
        n = int(len(audio))
        faded.append(audio[i] * (1 - (i/(n-1))))
    
    write_wav(faded, "faded.wav")

def echo():
    """Function that echos an audio clip"""
    user_prompt = (input("Enter file name: "))
    audio = read_wav(user_prompt)
    
    SOFTNESS_FACTOR = 0.3
    sample = audio
    softer = []
    
    for i in range(len(sample)):
        softer.append(sample[i] * SOFTNESS_FACTOR)

    shift_factor = int((len(sample)) / 8)
    
    sample_part2 = sample[shift_factor:]
    sample_part1 = sample[:shift_factor]
    softer_part2 = softer[0:int(len(softer)) - (shift_factor)]
    softer_part3= softer[int(len(softer)) - (shift_factor):]
    
    middle_list = []
    for i in range(len(sample_part2)):
        middle_list.append(softer_part2[i] + sample_part2[i])
    echo_list = sample_part1 + middle_list + softer_part3
    
    write_wav(echo_list, "echoed.wav")
   