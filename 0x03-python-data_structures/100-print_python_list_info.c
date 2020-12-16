#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i, size, allocated;
	PyObject *obj;

	allocated = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(obj)->tp_name);
	}

}
