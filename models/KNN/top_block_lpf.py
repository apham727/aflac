#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 19 15:23:48 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class top_block(gr.top_block):

    def __init__(self, input_filepath='/home/duncan/Documents/ML_Project/301-project.audio_train/301-project.audio_train/0a2a5c05.wav', output_filepath='/home/duncan/Documents/ML_Project/301-project.audio_train/filtered_files/0a2a5c05.wav'):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 4000, 500, firdes.WIN_HAMMING, 6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source(input_filepath, False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(output_filepath, 1, samp_rate, 8)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))

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
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 4000, 500, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--input-filepath", dest="input_filepath", type="string", default='/home/duncan/Documents/ML_Project/301-project.audio_train/301-project.audio_train/0a2a5c05.wav',
        help="Set /home/duncan/Documents/ML_Project/301-project.audio_train/301-project.audio_train/0a2a5c05.wav [default=%default]")
    parser.add_option(
        "", "--output-filepath", dest="output_filepath", type="string", default='/home/duncan/Documents/ML_Project/301-project.audio_train/filtered_files/0a2a5c05.wav',
        help="Set /home/duncan/Documents/ML_Project/301-project.audio_train/filtered_files/0a2a5c05.wav [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls(input_filepath=options.input_filepath, output_filepath=options.output_filepath)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
