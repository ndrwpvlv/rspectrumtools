# -*- coding: utf-8 -*-

import math
from .templates import SPECTRUM_REPORT


class ResponseSpectrum:

    def __init__(self, acc: list, dt: float, damping_ratio: float = 0.05, freq_max: float = None,
                 freq_step: float = None):
        self.acc = acc
        self.acc_max = max(self.acc)
        self.acc_min = min(self.acc)
        self.dt = dt
        self.time_range = [dt * sid for sid in range(len(self.acc))]
        self.time_end = dt * len(self.acc)
        self.damping_ratio = damping_ratio
        self.k_stab = 0.975  # Coefficient of solution stability
        self.freq_step = round(freq_step or 1.0 / self.time_end, 2)
        self.freq_min = round(1.0 / self.time_end, 2)
        self.freq_max = freq_max or round(self.k_stab * (1.0 / (math.pi * dt * (1.0 + 2.0 * damping_ratio))), 3)
        self.freq_range = self.make_freq_range()
        self.spec_acc = self.calc_response_spectrum()
        self.spec_beta = self.calc_beta_spectrum()

    def make_freq_range(self):
        int_scale = 1.0 / self.freq_step * 1000.0
        freq_min = self.freq_min
        freq_max = self.freq_max
        freq_step = self.freq_step
        freq_range = [float(f) / int_scale for f in range(
            int(freq_min * int_scale),
            int((freq_max + freq_step) * int_scale),
            int(freq_step * int_scale)
        )]
        return freq_range

    def calc_response_spectrum(self):
        n_steps = len(self.acc)
        spec_acel = []

        for freq in self.freq_range:
            omega_n = 2.0 * math.pi * freq
            c_damp = 2.0 * self.damping_ratio * omega_n
            disp = [0.0] * n_steps
            velo = [0.0] * n_steps
            acel = [0.0] * n_steps
            acel[0] = self.acc[0]

            for sid in range(1, n_steps):
                acel_eff = self.acc[sid] - c_damp * velo[sid - 1] - omega_n ** 2.0 * disp[sid - 1]
                velo[sid] = velo[sid - 1] + self.dt * acel_eff
                disp[sid] = disp[sid - 1] + self.dt * velo[sid]
                acel[sid] = omega_n ** 2.0 * disp[sid]

            spec_acel.append(max([abs(a) for a in acel]))
        return spec_acel

    def calc_beta_spectrum(self):
        acc_max_abs = max(abs(self.acc_max), abs(self.acc_min))
        spec_beta = [s / acc_max_abs for s in self.spec_acc]
        return spec_beta

    def make_report(self):
        report = SPECTRUM_REPORT.format(self.acc_max, self.acc_min, max(self.spec_acc), max(self.spec_beta))
        print(report)
        return report

    def write_spec_acc(self, filename: str = 'acc_rs.txt'):
        with open(filename, 'w') as file:
            for f, s in zip(self.freq_range, self.spec_acc):
                file.write(f'{f}\t{s}\n')
        print('File has been written')

    def write_spec_beta(self, filename: str = 'beta_rs.txt'):
        with open(filename, 'w') as file:
            for f, s in zip(self.freq_range, self.spec_beta):
                file.write(f'{f}\t{s}\n')
        print('File has been written')
