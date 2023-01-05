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
		async patchNewTicketStatusById(ctx, element) {
			console.log(element)
			ctx.commit('setNewTicketStatusById', element)
			await fetch('http://127.0.0.1:8000/api/appeal', {
				method: 'PATCH',
				body: {
					'id': element.elementId,
					'status': element.newStatus
				}
			})
		}
	}
})

// PATCH http://127.0.0.1:8000/api/appeal с телом
// {
// 	"id": 4,
// 	"status": "done"
// }
