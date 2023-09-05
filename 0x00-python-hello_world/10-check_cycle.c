#include<stdio.h>
#include<stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer beginningof  node
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list, *ft = list;

	while (s && ft->next)
	{
		s = s->next;
		ft = ft->next->next;
		if (s == ft)
			return (1);
	}
	return (0);
}
