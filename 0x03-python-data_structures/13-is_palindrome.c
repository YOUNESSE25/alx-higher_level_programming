#include<stdio.h>
#include<stdlib.h>
#include"lists.h"
/**
 * is_palindrome - check list palindrome
 * @head: head singly linked list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *dep = NULL, *fin = NULL;
	unsigned int i = 0, l = 0, l_cyc = 0, l_list = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	dep = *head;
	l = listint_l(dep);
	l_cyc = l * 2;
	l_list = l_cyc - 2;
	fin = *head;
	for (; i < l_cyc; i = i + 2)
	{
		if (dep[i].n != fin[l_list].n)
			return (0);
		l_list = l_list - 2;
	}
	return (1);
}
/**
 * get_nodeint - get node
 * @head: head of list
 * @index: index list
 * Return: node
 */
listint_t *get_nodeint(listint_t *head, unsigned int index)
{
	listint_t *cur = head;
	unsigned int iter_t = 0;

	if (head)
	{
		while (cur != NULL)
		{
			if (iter_t == index)
				return (cur);

			cur = cur->next;
			++iter_t;
		}
	}
	return (NULL);
}
/**
 * listint_l - linked list elements number
 * @h: linked list
 * Return: int
 */
size_t listint_l(const listint_t *h)
{
	int l = 0;

	while (h != NULL)
	{
		++l;
		h = h->next;
	}
	return (l);
}
