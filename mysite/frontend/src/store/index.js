import {createStore} from 'vuex';

export default createStore({
	state: () =>  ({
		tickets: []
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			state.tickets = tickets
		},
		setNewTicketStatusById(state, element){
			state.tickets.find((ticket) => ticket.id === element.elementId).status = element.newStatus
		}
	},
	actions: {
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('http://127.0.0.1:8000/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
				console.log(res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		},
		// csrftoken=7ci2ME64hzdWCM3Q0jNDy8efDq9v0twfUsD0Ltfj8vQJXijnluvPPE5MTBSHPFqS
		// _ym_uid=1662063435230778318; _ym_d=1662063435; _ym_isad=2; csrftoken=7ci2ME64hzdWCM3Q0jNDy8efDq9v0twfUsD0Ltfj8vQJXijnluvPPE5MTBSHPFqS
		async patchNewTicketStatusById(ctx, element) {
			const cookie = document.cookie
			console.log(cookie.substring(cookie.indexOf('csrftoken')))
			ctx.commit('setNewTicketStatusById', element)
			await fetch(`http://127.0.0.1:8000/api/appeal/${element.elementId}`, {
				method: 'PATCH',
				headers: {
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken'))
				},
				body: JSON.stringify({
					'status': element.newStatus
				})
			})
		}
	}
})
