"""Sound effect utility functions using Python audio libraries."""
import math
import struct
try:
    import pyaudio
    PYAUDIO_AVAILABLE = True
except ImportError:
    PYAUDIO_AVAILABLE = False
    print("Warning: pyaudio not available. Sound effects will be disabled.")


class SoundEffects:
    """Class to handle sound effect generation and playback."""
    
    def __init__(self):
        """Initialize the sound effects system."""
        self.sample_rate = 44100
        self.audio = None
        if PYAUDIO_AVAILABLE:
            try:
                self.audio = pyaudio.PyAudio()
            except Exception as e:
                print(f"Warning: Could not initialize PyAudio: {e}")
                self.audio = None
    
    def _generate_tone(self, frequency: float, duration: float, volume: float = 0.3) -> bytes:
        """Generate a tone with given frequency, duration, and volume."""
        num_samples = int(self.sample_rate * duration)
        samples = []
        
        for i in range(num_samples):
            # Apply exponential decay to volume
            decay = math.exp(-3 * i / num_samples)
            amplitude = volume * decay
            
            # Generate sine wave
            value = amplitude * math.sin(2 * math.pi * frequency * i / self.sample_rate)
            # Convert to 16-bit integer
            samples.append(int(value * 32767))
        
        # Convert to bytes
        return b''.join(struct.pack('<h', sample) for sample in samples)
    
    def _play_sound(self, audio_data: bytes):
        """Play audio data."""
        if not self.audio:
            return
        
        try:
            stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.sample_rate,
                output=True
            )
            stream.write(audio_data)
            stream.stop_stream()
            stream.close()
        except Exception as e:
            print(f"Warning: Could not play sound: {e}")
    
    def play_correct(self):
        """Play sound for correct answer (ascending notes: C5, E5, G5)."""
        if not self.audio:
            return
        
        # Generate three ascending tones
        tone1 = self._generate_tone(523.25, 0.1)  # C5
        tone2 = self._generate_tone(659.25, 0.1)  # E5
        tone3 = self._generate_tone(783.99, 0.1)  # G5
        
        combined = tone1 + tone2 + tone3
        self._play_sound(combined)
    
    def play_incorrect(self):
        """Play sound for incorrect answer (descending notes)."""
        if not self.audio:
            return
        
        # Generate two descending tones
        tone1 = self._generate_tone(200, 0.1)
        tone2 = self._generate_tone(150, 0.1)
        
        combined = tone1 + tone2
        self._play_sound(combined)
    
    def play_click(self):
        """Play a short click sound."""
        if not self.audio:
            return
        
        tone = self._generate_tone(800, 0.05, volume=0.2)
        self._play_sound(tone)
    
    def play_success(self):
        """Play success sound (ascending chord: C5, E5, G5, C6)."""
        if not self.audio:
            return
        
        # Generate four ascending tones
        tone1 = self._generate_tone(523.25, 0.1)   # C5
        tone2 = self._generate_tone(659.25, 0.1)   # E5
        tone3 = self._generate_tone(783.99, 0.1)   # G5
        tone4 = self._generate_tone(1046.50, 0.2)  # C6
        
        combined = tone1 + tone2 + tone3 + tone4
        self._play_sound(combined)
    
    def cleanup(self):
        """Clean up audio resources."""
        if self.audio:
            try:
                self.audio.terminate()
            except Exception:
                pass


# Global sound effects instance
sound_effects = SoundEffects()


def get_sound_effects() -> SoundEffects:
    """Get the global sound effects instance."""
    return sound_effects

