class Utils:
	def reversed(x: int) -> int:
		int_rev = int(str(int(x))[::-1])
		return int_rev

	def formatter(x: int) -> tuple[int, int]:
		x = int(x)
		binary_repr = bin(x).lstrip('-0b')
		octal_repr = oct(x).lstrip('-0o')
		binary_repr = int(binary_repr)
		octal_repr = int(octal_repr)
		return binary_repr, octal_repr
