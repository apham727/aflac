#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Dec  3 15:34:18 2019 
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class top_block(gr.top_block):

    def __init__(self, frac_dem=1, frac_num=1, input_filepath='//home/duncan/Documents/ML_Project/filtered_files_short/0a2a5c05.wav', output_filepath='//home/duncan/Documents/ML_Project/filtered_files_short_resampled/0a2a5c05.wav'):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.frac_dem = frac_dem
        self.frac_num = frac_num
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=frac_dem,
                decimation=frac_num,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source(input_filepath, False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(output_filepath, 1, samp_rate, 8)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_wavfile_sink_0, 0))

    def get_frac_dem(self):
        return self.frac_dem

    def set_frac_dem(self, frac_dem):
        self.frac_dem = frac_dem

    def get_frac_num(self):
        return self.frac_num

    def set_frac_num(self, frac_num):
        self.frac_num = frac_num

    def get_input_filepath(self):
        return self.input_filepath

    def set_input_filepath(self, input_filepath):
        self.input_filepath = input_filepath

    def get_output_filepath(self):
        return self.output_filepath

    def set_output_filepath(self, output_filepath):
        self.output_filepath = output_filepath
        self.blocks_wavfile_sink_0.open(self.output_filepath)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--frac-dem", dest="frac_dem", type="intx", default=1,
        help="Set frac_dem [default=%default]")
    parser.add_option(
        "", "--frac-num", dest="frac_num", type="intx", default=1,
        help="Set frac_num [default=%default]")
    parser.add_option(
        "", "--input-filepath", dest="input_filepath", type="string", default='//home/duncan/Documents/ML_Project/filtered_files_short/0a2a5c05.wav',
        help="Set //home/duncan/Documents/ML_Project/filtered_files_short/0a2a5c05.wav [default=%default]")
    parser.add_option(
        "", "--output-filepath", dest="output_filepath", type="string", default='//home/duncan/Documents/ML_Project/filtered_files_short_resampled/0a2a5c05.wav',
        help="Set //home/duncan/Documents/ML_Project/filtered_files_short_resampled/0a2a5c05.wav [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(frac_dem=options.frac_dem, frac_num=options.frac_num, input_filepath=options.input_filepath, output_filepath=options.output_filepath)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
