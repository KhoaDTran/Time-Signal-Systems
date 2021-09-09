def analyze(b, a, title):
  b = np.reshape(b, -1)
  a = np.reshape(a, -1)
  fig = plt.figure(figsize = (10, 8))
  fig.suptitle(title, fontsize = 'x-large')
  fig.subplots_adjust(hspace = 0.5, wspace = 0.3)

  # Plot frequency response
  w, h = signal.freqz(b, a, 1024)
  w_majors = np.array([0, 0.2, 0.4, 0.6, 0.8, 1]) * np.pi
  w_labels = ['0', r'$0.2\pi$', r'$0.4\pi$',
              r'$0.6\pi$', r'$0.8\pi$', r'$\pi$']
  ax = fig.add_subplot(221)
  ax.plot(w, 20 * np.log10(np.abs(h)))
  ax.set_xticks(w_majors)
  ax.set_xticklabels(w_labels)
  ax.set_title('Magnitude Response')
  ax.set_xlabel('Frequency [rad]')
  ax.set_ylabel('Gain [dB]')
  ax = fig.add_subplot(222)
  ax.plot(w, np.rad2deg(np.unwrap(np.angle(h))))
  ax.set_xticks(w_majors)
  ax.set_xticklabels(w_labels)
  ax.set_title('Phase Response')
  ax.set_xlabel('Frequency [rad]')
  ax.set_ylabel('Phase [deg]')

  # Plot impulse response
  x = np.zeros(50); x[0] = 1
  y = signal.lfilter(b, a, x)
  ax = fig.add_subplot(223)
  ax.stem(np.arange(len(y)), y)
  ax.set_title('Impulse Response')
  ax.set_xlabel('Time')
  ax.set_ylabel('Output')

  # Plot poles & zeros
  n_taps = max(len(b), len(a))
  b = np.pad(b, (0, n_taps - len(b)), 'constant')
  a = np.pad(a, (0, n_taps - len(a)), 'constant')
  z, p, k = signal.tf2zpk(b, a)
  ax = fig.add_subplot(224, projection = 'polar')
  ax.plot(np.angle(p), np.abs(p), 'x')
  ax.plot(np.angle(z), np.abs(z), 'o', markerfacecolor = 'none')
  lines, labels = ax.set_rgrids([1])
  for line in lines: line.set_color('black')
  ax.set_thetagrids([0, 90, 180, 270], ['Re(z)', 'Im(z)'])
  ax.set_rlabel_position(0)
  ax.spines['polar'].set_visible(False)
  ax.set_title('Poles & Zeros', y = 1.1)
