class OpticalElement(object):
	def __call__(self, wavefront):
		raise self.forward(wavefront)
	
	def forward(self, wavefront):
		raise NotImplementedError()
	
	def backward(self, wavefront):
		raise NotImplementedError()

class Detector(object):
	def integrate(self, wavefront):
		raise NotImplementedError()
	
	def read_out(self):
		raise NotImplementedError()
	
	def reset(self):
		raise NotImplementedError()