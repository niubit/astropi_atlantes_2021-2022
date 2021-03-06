import numpy as np
  
fastiecm_wool_index = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [8],
                                [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8],
                                [8], [8], [8], [8], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7],
                                [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7],
                                [7], [7], [7], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8],
                                [8], [8], [8], [8], [8], [8], [8], [8], [0], [0], [0], [0], [0], [0], [0],
                                [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
                                [0], [0], [0], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8], [8],
                                [8], [8], [8], [8], [8], [7], [7], [7], [7], [7], [7], [7], [7], [7], [7],
                                [7], [7], [9], [9], [9], [9], [3], [3], [3], [3], [3], [3], [3], [3], [3],
                                [3], [3], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [5],
                                [5], [5], [5], [5], [5], [5], [5], [5], [5], [5], [4], [4], [4], [4], [4],
                                [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4],
                                [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4], [4],
                                [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1],
                                [1], [1], [1], [1], [1], [14], [14], [14], [14], [14], [14], [14], [14],
                                [14], [14], [14], [14], [14], [14], [14], [14], [14], [14], [2], [2], [2],
                                [2], [2], [2], [2], [2]], dtype=np.uint8)
 
fastiecm_wool = np.array([[[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]], [[228, 228, 228]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]], [[160, 167, 167]],
                          [[160, 167, 167]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]], [[65, 65, 65]],
                          [[65, 65, 65]], [[145, 113, 38]], [[145, 113, 38]], [[145, 113, 38]],
                          [[145, 113, 38]], [[210, 135, 99]], [[210, 135, 99]], [[210, 135, 99]],
                          [[210, 135, 99]], [[210, 135, 99]], [[210, 135, 99]], [[210, 135, 99]],
                          [[210, 135, 99]], [[210, 135, 99]], [[210, 135, 99]], [[210, 135, 99]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]],
                          [[46, 186, 57]], [[46, 186, 57]], [[46, 186, 57]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]], [[28, 181, 194]],
                          [[28, 181, 194]], [[28, 181, 194]], [[53, 126, 234]], [[53, 126, 234]],
                          [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]],
                          [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]],
                          [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]],
                          [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]], [[53, 126, 234]],
                          [[53, 126, 234]], [[53, 126, 234]], [[39, 43, 158]], [[39, 43, 158]],
                          [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]],
                          [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]],
                          [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]],
                          [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]], [[39, 43, 158]],
                          [[201, 73, 190]], [[201, 73, 190]], [[201, 73, 190]], [[201, 73, 190]],
                          [[201, 73, 190]], [[201, 73, 190]], [[201, 73, 190]], [[201, 73, 190]]], dtype=np.uint8)
