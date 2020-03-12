#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar 12 11:01:14 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self, uri='ip:10.43.156.103'):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.uri = uri

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.fs = fs = 1000
        self.FMCOMMS_samp_rate = FMCOMMS_samp_rate = 2084000
        self.FMCOMMS_RFband = FMCOMMS_RFband = 20e6
        self.FMCOMMS_LO = FMCOMMS_LO = 2.4e9

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0_1 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0_1.win)
        self.channels_phase_noise_gen_0 = channels.phase_noise_gen(0.69, 0.1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.channels_phase_noise_gen_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.channels_phase_noise_gen_0, 0), (self.blocks_complex_to_float_0, 0))

    def get_uri(self):
        return self.uri

    def set_uri(self, uri):
        self.uri = uri

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_1.set_sample_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs

    def get_FMCOMMS_samp_rate(self):
        return self.FMCOMMS_samp_rate

    def set_FMCOMMS_samp_rate(self, FMCOMMS_samp_rate):
        self.FMCOMMS_samp_rate = FMCOMMS_samp_rate

    def get_FMCOMMS_RFband(self):
        return self.FMCOMMS_RFband

    def set_FMCOMMS_RFband(self, FMCOMMS_RFband):
        self.FMCOMMS_RFband = FMCOMMS_RFband

    def get_FMCOMMS_LO(self):
        return self.FMCOMMS_LO

    def set_FMCOMMS_LO(self, FMCOMMS_LO):
        self.FMCOMMS_LO = FMCOMMS_LO


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--uri", dest="uri", type="string", default='ip:10.43.156.103',
        help="Set URI [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(uri=options.uri)
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
