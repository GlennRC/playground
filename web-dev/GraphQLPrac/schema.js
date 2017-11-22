const {
    GraphQLObjectType,
    GraphQLString,
    GraphQLInt,
    GraphQLSchema,
    GraphQLList,
    GraphQLNonNull
} = require("graphql");


// Hardcoded data
const customers = [
    {id:"1", name:"Glenn Contreras", email:"glennrcontreras@gmail.com", age:26},
    {id:"2", name:"Mailyng Blair", email:"mailyng23@gmail.com", age:26},
    {id:"3", name:"John Doe", email:"johndoe@gmail.com", age:35}
]

// Customer Type
const CustomerType = new GraphQLObjectType({
    name: "Customer",
    fields: () => ({
        id: {type:GraphQLString},
        name: {type:GraphQLString},
        email: {type:GraphQLString},
        age: {type:GraphQLInt}
    })
});


// Root Query
const RootQuery = new GraphQLObjectType({
    name: "RootQueryType",
    fields: {
        customer: {
            type:CustomerType,
            args: {
                id:{type:GraphQLString}
            },
            resolve(parentValue, args){
                for(let i=0;i<customers.length;i++) {
                    if(customers[i].id == args.id) {
                        return customers[i];
                    }
                }
            }
        },
        customers: {
            type: new GraphQLList(CustomerType),
            resolve(parentValue, args) {
                return customers;
            }
        }
    }
})

module.exports = new GraphQLSchema({
    query: RootQuery
});