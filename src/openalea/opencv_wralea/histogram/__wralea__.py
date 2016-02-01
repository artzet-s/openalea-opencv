# This file has been automatically generated by pkg_builder

from openalea.core import *

__name__ = 'openalea.opencv.histogram'
__version__ = '1.0.0'
__license__ = 'CeCILL-C'
__author__ = 'M.Mielewczik, C.Fournier, C. Pradal'
__institutes__ = None
__description__ = ''
__url__ = 'http://openalea.gforge.inria.fr'

__editable__ = 'True'
__icon__ = 'histogram.png'
__alias__ = []


__all__ = ['opencv2_grayscalehistogram',]



opencv2_grayscalehistogram = Factory(name='grayscalehistogram',
                authors=' (M.Mielewczik)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.nodes',
                nodeclass='grayscalehistogram',
                #inputs=[{'interface': IFileStr, 'name': 'Image'}],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )

