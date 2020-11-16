let data_structure = '{"name":"","email":"","phone":"","country":"","area":"","street":"","house":"","specific_directions":"","shipping":0,"cart":[]}'

class Structure{

    constructor(){
        let data_in_browser = localStorage.getItem("data") ? true : false
        if(!data_in_browser){
            localStorage.setItem("data",data_structure)
        }
        this.data = JSON.parse(localStorage.getItem("data"))
    }

    edit_property (name,value){
        this.data[name] = value
        this.save()

    }

    add_item (pk,product_name,flavour_name,price,quantity){
        let item = this.get_item(pk)
        if(item){
            item.quantity = quantity
        }
        else{
            item = {pk,product_name,flavour_name,price,quantity}
            this.data.cart.push(item)
        }
        this.save()
        return item
    }

    get_item(pk){
        let index = this.get_index(pk)
        if(index.found){
            return this.data.cart[index.index]
        }
        return false
    }

    remove_item (pk){
        let index = this.get_index(pk)
        if(index.found){
            this.data.cart.pop(index.index)
        }
        this.save()
    }

    get_index(pk){
        let result = {found:false,index:-1}
        this.data.cart.forEach((item,index)=>{
            if(item.pk === pk){
                result.found = true 
                result.index = index
                return
            }
        })
        return result
    }

    get_quantity (pk){
        let item = this.get_item(pk)
        if(item){
            return item.quantity
        }
        return 1
    }

    get_quantites(){
        let q = 0
        this.data.cart.forEach((item,index)=>{
            q += item.quantity
        })
        return q
    }

    get_total(){
        let q = 0
        this.data.cart.forEach((item,index)=>{
            q += item.price * item.quantity
        })
        if(this.data.shipping){
            q+= this.data.shipping
        }
        return q    
    }

    increment (pk){
        let index = this.get_index(pk)
        if(index.found){
            let item = this.data.cart[index.index]
            item.quantity += 1
            this.save()
            return true
        }
        return false
    }

    decrement(pk){
        let index = this.get_index(pk)
        if(index.found){
            let item = this.data.cart[index.index]
            item.quantity -= 1
            this.save()
            return true
        }
        return false
    }

    eligible_for_order(){
        return this.data.cart.length > 0 ? true : false
    }

    eligible_for_confirm(){
        if (this.eligible_for_order()){
            if(this.data.name && this.data.email && this.data.phone && this.data.area && this.data.street && this.data.house) {
                return true
            }
        }
        return false
    }

    save(){
        localStorage.setItem("data",JSON.stringify(this.data))
    }

    reset_cart(){
        this.data.cart = []
        this.save()
    }
}

let ST = new Structure()
