# Load a WAV file.
# Return the sampling rate and the sample array.
def wav_load(file_name):
  # Load the raw data.
  sr, data = wav.read(file_name)
  # Only use the first channel.
  if data.ndim > 1:
    data = data[:, 0]
  # Convert to float32 quantization.
  kind = data.dtype.kind
  bits = data.dtype.itemsize * 8
  data = data.astype('float32')
  if kind == 'i' or kind == 'u':
    data = data / 2 ** (bits - 1)
    if kind == 'u':
      data = data - 1
  return sr, data
