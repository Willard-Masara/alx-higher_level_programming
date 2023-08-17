#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *data = PyBytes_AsString(p);
    
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);

    Py_ssize_t limit = size < 10 ? size : 10;

    printf("  first %ld bytes:", limit);

    for (Py_ssize_t i = 0; i < limit; i++)
    {
        printf(" %02hhx", data[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *obj = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(obj)->tp_name;

        printf("Element %ld: %s\n", i, type_name);

        if (PyBytes_Check(obj))
        {
            print_python_bytes(obj);
        }
    }
}
