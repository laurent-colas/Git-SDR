#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar 12 12:07:06 2020
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
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
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0_1.win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(1, ([1,1,1,1]))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c(uri, int(FMCOMMS_LO), int(FMCOMMS_samp_rate), int(FMCOMMS_RFband), True, False, 0x8000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", '', True)
        self.high_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.high_pass(
        	1, samp_rate, samp_rate/100, samp_rate/1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-0.0001, 0.0001, 0)
        self.blocks_probe_rate_0 = blocks.probe_rate(gr.sizeof_float*1, 500.0, 0.15)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_probe_rate_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_threshold_ff_0, 0), (self.wxgui_scopesink2_0_1, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.iio_fmcomms2_source_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.high_pass_filter_0, 0))

    def get_uri(self):
        return self.uri

    def set_uri(self, uri):
        self.uri = uri

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_1.set_sample_rate(self.samp_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.samp_rate/100, self.samp_rate/1000, firdes.WIN_HAMMING, 6.76))

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs

    def get_FMCOMMS_samp_rate(self):
        return self.FMCOMMS_samp_rate

    def set_FMCOMMS_samp_rate(self, FMCOMMS_samp_rate):
        self.FMCOMMS_samp_rate = FMCOMMS_samp_rate
        self.iio_fmcomms2_source_0.set_params(int(self.FMCOMMS_LO), int(self.FMCOMMS_samp_rate), int(self.FMCOMMS_RFband), True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_FMCOMMS_RFband(self):
        return self.FMCOMMS_RFband

    def set_FMCOMMS_RFband(self, FMCOMMS_RFband):
        self.FMCOMMS_RFband = FMCOMMS_RFband
        self.iio_fmcomms2_source_0.set_params(int(self.FMCOMMS_LO), int(self.FMCOMMS_samp_rate), int(self.FMCOMMS_RFband), True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", '', True)

    def get_FMCOMMS_LO(self):
        return self.FMCOMMS_LO

    def set_FMCOMMS_LO(self, FMCOMMS_LO):
        self.FMCOMMS_LO = FMCOMMS_LO
        self.iio_fmcomms2_source_0.set_params(int(self.FMCOMMS_LO), int(self.FMCOMMS_samp_rate), int(self.FMCOMMS_RFband), True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", '', True)


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
