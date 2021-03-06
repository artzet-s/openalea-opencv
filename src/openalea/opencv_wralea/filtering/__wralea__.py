# This file has been automatically generated by pkg_builder

from openalea.core import *

__name__ = 'openalea.opencv.filtering'
__version__ = '1.0.0'
__license__ = 'CeCILL-C'
__author__ = 'M.Mielewczik, C.Fournier, C. Pradal'
__institutes__ = None
__description__ = ''
__url__ = 'http://openalea.gforge.inria.fr'

__editable__ = 'True'
__icon__ = 'blurring.png'
__alias__ = []

__all__ = []

bordertype = ['BORDER_DEFAULT','BORDER_CONSTANT', 'BORDER_ISOLATED', 'BORDER_REFLECT', 'BORDER_REFLECT101', 'BORDER_REFLECT_101','BORDER_REPLICATE', 'BORDER_TRANSPARENT', 'BORDER_WRAP']               
kernelshapes = ['MORPH_RECT', 'MORPH_CROSS','MORPH_ELLIPSE']

opencv2_erode = Factory(name='erode',
                authors=' (M.Mielewczik, C.Fournier)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='erode',
                inputs=[{'interface': None, 'name': 'Image'},
                {'interface': IEnumStr(enum=kernelshapes), 'name': 'Kernel shape', 'value':'MORPH_CROSS'},
                {'interface': IInt, 'name': 'Kernel size', 'value':3},
                {'interface': IInt, 'name': 'Iterations', 'value':1},],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_erode')

opencv2_dilate = Factory(name='dilate',
                authors=' (M.Mielewczik, C.Fournier)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='dilate',
                inputs=[{'interface': None, 'name': 'Image'},
                {'interface': IEnumStr(enum=kernelshapes), 'name': 'Kernel shape', 'value':'MORPH_CROSS'},
                {'interface': IInt, 'name': 'Kernel size', 'value':3},
                {'interface': IInt, 'name': 'Iterations', 'value':1},],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_dilate')

opencv2_open = Factory(name='open',
                authors=' (C.Fournier)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='open',
                inputs=[{'interface': None, 'name': 'Image'},
                {'interface': IEnumStr(enum=kernelshapes), 'name': 'Kernel shape', 'value':'MORPH_CROSS'},
                {'interface': IInt, 'name': 'Kernel size', 'value':3},
                {'interface': IInt, 'name': 'Iterations', 'value':1},],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_open')

opencv2_close = Factory(name='close',
                authors=' (C.Fournier)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='close',
                inputs=[{'interface': None, 'name': 'Image'},
                {'interface': IEnumStr(enum=kernelshapes), 'name': 'Kernel shape', 'value':'MORPH_CROSS'},
                {'interface': IInt, 'name': 'Kernel size', 'value':3},
                {'interface': IInt, 'name': 'Iterations', 'value':1},],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_close')

opencv2_morphological_skeleton = Factory(name='morphological_skeleton',
                authors=' (C. Fournier)',
                description='Compute Morphologigal skeleton on a binary image',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='morphological_skeleton',
                inputs=[{'interface': None, 'name': 'Image'}],
                outputs=({'interface': None, 'name': 'skeleton'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_morphological_skeleton')
              
opencv2_bilateralFilter = Factory(name='bilateralFilter',
                authors=' (M.Mielewczik)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.nodes',
                nodeclass='bilateralFilter',
                inputs=[{'interface': None, 'name': 'Image'},
                        {'interface': IInt(1,3), 'name':'d', 'value':(3)}, 
                        {'interface': IInt(1,3), 'name':'sigmaColor', 'value':(1)},
                        {'interface': IInt(1,3), 'name':'sigmaSpace', 'value':(1)},
                        {'interface': IEnumStr(enum=bordertype), 'name': 'BorderType', 'value': 'BORDER_DEFAULT'}],
                # inputs=[{'interface': IFileStr, 'name': 'Image'},
                        # {'interface': IInt(-1,1,3,5), 'name':'d', 'value':(3)},
                        # {'interface': IInt(1,21), 'name': 'sigmaColor', 'value':(5)},
                        # {'interface': IInt(1,21), 'name': 'sigmaSpace', 'value':(5)},
                        # {'interface': IEnumStr(enum=bordertype), 'name': 'BorderType', 'value': 'BORDER_DEFAULT'},],
                outputs=[{'interface': None, 'name': 'image'},],
                widgetmodule=None,
                widgetclass=None,
               )    
__all__.append('opencv2_bilateralFilter')
               
opencv2_Laplacian = Factory(name='Laplacian',
                authors=' (M.Mielewczik)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.nodes',
                nodeclass='Laplacian',
                inputs=[{'interface': None, 'name': 'Image'},
                        {'interface': IInt(1,3), 'name':'d', 'value':(3)}, 
                        {'interface': IInt(1,3), 'name':'sigmaColor', 'value':(1)},
                        {'interface': IInt(1,3), 'name':'sigmaSpace', 'value':(1)},
                        {'interface': IEnumStr(enum=bordertype), 'name': 'BorderType', 'value': 'BORDER_DEFAULT'}],
                outputs=({'interface': None, 'name': 'image'},),
                widgetmodule=None,
                widgetclass=None,
               )    

__all__.append('opencv2_Laplacian')

opencv2_medianBlur = Factory(name='medianBlur',
                authors=' (M.Mielewczik)',
                description='Bur image with a gaussian filter',
                category='Image Processing',
                nodemodule='cv2',
                nodeclass='medianBlur',
                #inputs=[{'interface': IFileStr, 'name': 'Image'}],
                outputs=({'interface': None, 'name': 'out'},),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_medianBlur')

# (CF) for Sharr/Sobel, docstring/output names seems outdated
opencv2_Scharr = Factory(name='Scharr',
                authors=' (M.Mielewczik)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='Scharr',
                inputs=[{'interface': None, 'name': 'Image'},
                        {'interface': IInt(1,3), 'name':'dx', 'value':(0)},
                        {'interface': IInt(1,3), 'name':'dy', 'value':(1)},
                        {'interface': IEnumStr(enum=bordertype), 'name': 'BorderType', 'value': 'BORDER_DEFAULT'}],
                outputs=({'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'cropped'},
                        {'interface': None, 'name': 'cropped'}),
                widgetmodule=None,
                widgetclass=None,
               )
__all__.append('opencv2_Scharr')             

opencv2_Sobel = Factory(name='Sobel',
                authors=' (M.Mielewczik)',
                description='',
                category='Image Processing',
                nodemodule='openalea.opencv.extension',
                nodeclass='Sobel',
                inputs=[{'interface': None, 'name': 'Image'},
                        {'interface': IInt(1,3), 'name':'dx', 'value':(0)}, 
                        {'interface': IInt(1,3), 'name':'dy', 'value':(1)}, 
                        {'interface': IEnumStr(enum=bordertype), 'name': 'BorderType', 'value': 'BORDER_DEFAULT'}],
                outputs=({'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'image'},
                        {'interface': None, 'name': 'cropped'},
                        {'interface': None, 'name': 'cropped'}),
                widgetmodule=None,
                widgetclass=None,
               )
			   
__all__.append('opencv2_Sobel')

               


