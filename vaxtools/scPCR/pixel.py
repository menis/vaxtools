#!/usr/bin/env python
# filename: pixel.py


#
# Copyright (c) 2015 Bryan Briney
# License: The MIT license (http://opensource.org/licenses/MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from abutils.core.sequence import Sequence
from abutils.utils.alignment import mafft


def make_pixel(seqs, ffile, consentroid, cluster_seq_ids=None):
	nuc_vals = {'-': 0,
				'A': 1,
				'C': 2,
				'G': 3,
				'T': 4}
	cmap = ListedColormap(['w', '#E12427', '#3B7FB6', '#63BE7A', '#E1E383', 'k'])
	data = []
	if cluster_seq_ids is None:
		cluster_seq_ids = []
	aligned_seqs = _pixel_msa(consentroid, seqs)
	for seq in aligned_seqs:
		if seq.id == consentroid.id:
			sequence = 'XXXXXXXXXX--' + seq.sequence
		elif seq.id in cluster_seq_ids:
			sequence = '---XXXX-----' + seq.sequence
		else:
			sequence = '------------' + seq.sequence
		seq_data = [nuc_vals.get(res.upper(), 6) for res in sequence]
		data.append(seq_data)
	mag = (magnitude(len(data[0])) + magnitude(len(data))) / 2
	x_dim = len(data[0]) / 10**mag
	y_dim = len(data) / 10**mag
	plt.figure(figsize=(x_dim, y_dim), dpi=100)
	plt.imshow(data, cmap=cmap, interpolation='none')
	plt.axis('off')
	plt.savefig(ffile, bbox_inches='tight', dpi=400)
	plt.close()


def _pixel_msa(consentroid, seqs):
	seqs_for_aln = seqs + [consentroid]
	aln = mafft(seqs_for_aln)
	return [Sequence(s) for s in aln]

	# fasta = ''
	# if consentroid is not None:
	# 	fasta += '>consentroid\n{}\n'.format(consentroid)
	# fasta += '\n'.join(['>{}\n{}'.format(s[0], s[1]) for s in seqs])

	# fasta_file = os.path.join(temp_dir, 'alignment_input.fasta')
	# alignment_file = os.path.join(temp_dir, 'alignment.aln')
	# open(fasta_file, 'w').write(fasta)

	# alignment_file = do_msa(fasta_file, alignment_file)

	# # if len(seqs) < 100:
	# # 	muscle_cline = 'muscle -clwstrict'
	# # elif len(seqs) < 1000:
	# # 	muscle_cline = 'muscle -clwstrict -maxiters 2'
	# # else:
	# # 	muscle_cline = 'muscle -clwstrict -maxiters 1 -diags'
	# # muscle = sp.Popen(str(muscle_cline),
	# # 				  stdin=sp.PIPE,
	# # 				  stdout=sp.PIPE,
	# # 				  stderr=sp.PIPE,
	# # 				  universal_newlines=True,
	# # 				  shell=True)
	# # alignment = muscle.communicate(input=fasta)[0]
	# # aln = AlignIO.read(StringIO(alignment), 'clustal')
	# aln = AlignIO.read(open(alignment_file), 'clustal')
	# aln_seqs = []
	# for record in aln:
	# 	aln_seqs.append((record.id, str(record.seq)))

	# os.unlink(fasta_file)
	# os.unlink(alignment_file)

	# return aln_seqs


def magnitude(x):
	return int(math.log10(x))
