import {createStore} from 'vuex';
import {format} from 'date-fns';

export default createStore({
	state: () => ({
		tickets: [],
		user: null,
		filterHelpType: [],
		allUsers: [],
		allStatistic: {
			'optionStatistic': [],
			'statusStatistic': {
				'new': 0,
				'work': 0,
				'done': 0,
				'archive': 0
			},
			'total': 0
		},
		allUserStatistic: [],
		monthUserStatistic: {},
		monthStatistic: {},
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			tickets.forEach((ticket) => {
				const parsedDateArray = ticket.create_date.split('-')
				const dateObject = new Date(Number(parsedDateArray[2]), Number(parsedDateArray[1] - 1), Number(parsedDateArray[0]))
				ticket.create_date = format(dateObject, 'dd.MM.yyyy')
			})
			state.tickets = tickets
		},
		setNewTicketStatusById(state, element) {
			state.tickets.find((ticket) => ticket.id === element.elementId).status = element.newStatus
		},
		setUser(state, user) {
			state.user = user
		},
		deleteTicket(state, ticketId) {
			state.tickets = state.tickets.filter((ticket) => ticket.id !== ticketId)
		},
		setAllUsers(state, users) {
			state.allUsers = users
		},
		setNewStatusToTicket(state, element) {
			state.tickets.find((ticket) => ticket.id === element.id).status = 'new'
		},
		setAllStatistic(state, statistic) {
			state.allStatistic['optionStatistic'] = Array.from(Object.values(statistic.option))
			state.allStatistic['statusStatistic'] = statistic.status
			state.allStatistic['total'] = statistic.total
		},
		setAllUserStatistic(state, statistic) {
			state.allUserStatistic = statistic
		},
		setArchiveStatus(state, element) {
			state.tickets.find((ticket) => ticket.id === element.id).status = 'archive'
		},
		setMonthUserStatistic(state, data) {
			state.monthUserStatistic = data
		},
		setMonthStatistic(state, data) {
			state.monthStatistic = data
		}
	},
	actions: {
		async getUser(ctx) {
			const ans = await fetch('http://127.0.0.1:8000/api/user', {method: 'GET'})
			if (ans.ok) {
				const res = await ans.json()
				ctx.commit('setUser', res)
			} else {
				console.log(`Не удалось получить пользователя`)
			}
		},
		async getAllUsers(ctx) {
			const ans = await fetch('http://127.0.0.1:8000/api/all-users', {method: 'GET'})
			if (ans.ok) {
				ctx.commit('setAllUsers', await ans.json())
			} else {
				console.log(`Не удалось получить сотрудников`)
			}
		},
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		},
		async patchTicketStatusById(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.elementId}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': element.newStatus
				})
			})
			if (res.ok) {
				ctx.commit('setNewTicketStatusById', element)
			} else {
				console.log(`Не удалось обновить статус тикета с ID: ${element.id}`)
			}
		},
		async patchTicketNotes(ctx, data) {
			const cookie = document.cookie
			if (data.element.notes !== data.newNote) {
				const res = await fetch(`http://127.0.0.1:8000/api/appeal/${data.element.id}`, {
					method: 'PATCH',
					headers: {
						'Content-Type': 'application/json',
						'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
					},
					body: JSON.stringify({
						'notes': data.newNote
					})
				})
				if (!res.ok) {
					console.log(`Не удалось обновить заметку тикета с ID: ${data.element.id}`)
				}
			}
		},
		async deleteTicketById(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
			})
			if (res.ok) {
				ctx.commit('deleteTicket', element.id)
			} else {
				console.log(`Не удалось удалить тикет ${element.id}`)
			}
		},
		async pathTicketFlag(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'flag': !element.flag
				})
			})
			if (!res.ok) {
				console.log(`Не удалось отметить тикет ${element.id}`)
			}
		},
		async moveFromArchiveToNew(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': 'new'
				})
			})
			if (res.ok) {
				ctx.commit('setNewStatusToTicket', element)
			} else {
				console.log(`Не удалось обновить статус тикета с ID: ${element.id}`)
			}
		},
		async fetchAllStatistic(ctx) {
			const ans = await fetch('http://127.0.0.1:8000/api/statistics', {method: 'GET'})
			const ans2 = await fetch('http://127.0.0.1:8000/api/statistics-users', {method: 'GET'})
			if (ans.ok && ans2.ok) {
				const res = await ans.json()
				const res2 = await ans2.json()
				ctx.commit('setAllStatistic', res)
				ctx.commit('setAllUserStatistic', res2)
			} else {
				console.log(`Не удалось получить статистику за все время`)
			}
		},
		async patchUserOnTicket(ctx, param) {
			const cookie = document.cookie
			await fetch(`http://127.0.0.1:8000/api/appeal/${param.selectedTicket}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'user_id': param.newSelectedUser
				})
			})
		},
		async moveTicketToArchive(ctx, element) {
			const cookie = document.cookie
			const res = await fetch(`http://127.0.0.1:8000/api/appeal/${element.id}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': 'archive'
				})
			})
			if (res.ok) {
				ctx.commit('setArchiveStatus', element)
			} else {
				console.log(`Не удалось обновить статус тикета с ID: ${element.id}`)
			}
		},
		async fetchMonthStatistic(ctx, date) {
			const res = await fetch(`http://127.0.0.1:8000/api/statistics-per-month/${date.year}/${date.month}`, {method: 'GET'})
			if (res.ok) {
				ctx.commit('setMonthStatistic', await res.json())
			} else {
				console.log(`Не удалось получить статистику за месяц: ${date}`)
			}
		},
		async fetchMonthUserStatistic(ctx, date) {
			const res = await fetch(`http://127.0.0.1:8000/api/statistics-user-per-month/${date.year}/${date.month}`, {method: 'GET'})
			if (res.ok) {
				ctx.commit('setMonthUserStatistic', await res.json())
			} else {
				console.log(`Не удалось получить статистику за месяц по юзерам: ${date}`)
			}
		}
	}
})
