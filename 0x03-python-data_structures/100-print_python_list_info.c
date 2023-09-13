#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - print list info
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	pyObject *item;
	pyListObject *list;
	int size, alloc, i = 0;

	size = Py_size(p);
	list = (PyListObject *)p;
	alloc = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n, i, Py_TYPE(item)->tp_name);
	}
}
