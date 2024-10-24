# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from .config import Config


def plot_acc(time: list, acc: list, image_filename: str = 'acc_plot.png',
             title: str = 'Accelerogram', x_label: str = 'Time, s',
             y_label: str = 'Acceleration, m/s2', dpi=Config.PLOT_DPI):
    plt.figure(figsize=(12, 6))
    plt.plot(time, acc)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.savefig(image_filename, dpi=dpi)
    plt.show()


def plot_acc_3x(acc_txyz: dict, image_filename: str = 'acc_xyz_plot.png',
                title: str = 'Accelerogram', x_label: str = 'Time, s',
                y_label: str = 'Acceleration, m/s2', dpi=Config.PLOT_DPI):
    plt.figure(figsize=(12, 6))
    plt.plot(acc_txyz['time'], acc_txyz['x'], label='Acel. X')
    plt.plot(acc_txyz['time'], acc_txyz['y'], label='Acel. Y')
    plt.plot(acc_txyz['time'], acc_txyz['z'], label='Acel. Z')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.savefig(image_filename, dpi=dpi)
    plt.show()


def plot_spectrum(freqs: list, response_spectrum: list,
                  image_filename: str = 'rs_plot.png',
                  title: str = 'Response spectrum', x_label: str = 'Frequency, Hz',
                  y_label: str = 'Acceleration, m/s2', dpi=Config.PLOT_DPI):
    plt.figure(figsize=(12, 6))
    plt.plot(freqs, response_spectrum)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.savefig(image_filename, dpi=dpi)
    plt.show()


def plot_spectrum_3x(rs_fxyz: dict,
                     image_filename: str = 'rs_xyz_plot.png',
                     title: str = 'Response spectrum', x_label: str = 'Frequency, Hz',
                     y_label: str = 'Acceleration, m/s2', dpi=Config.PLOT_DPI):
    plt.figure(figsize=(12, 6))
    plt.plot(rs_fxyz['freq'], rs_fxyz['x'], label='Spectrum X')
    plt.plot(rs_fxyz['freq'], rs_fxyz['y'], label='Spectrum Y')
    plt.plot(rs_fxyz['freq'], rs_fxyz['z'], label='Spectrum Z')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.legend()
    plt.savefig(image_filename, dpi=dpi)
    plt.show()
