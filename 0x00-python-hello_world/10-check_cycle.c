#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer beginningof  node
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *ft;

	if (list == NULL || list->next == NULL)
		return (0);
	s = list;
	ft = s->next;
	while (s != NULL && ft->next != NULL &&
			s->next->next != NULL)
	{
		if (s == ft)
		{
			return (1);
		}
		s = s->next;
		ft = ft->next->next;
	}
	return (0);
}
