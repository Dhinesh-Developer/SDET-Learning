export class DashboardPage{
    constructor(page) {
        this.page = page
        this.heading = page.locater("h2")
        this.logoutButton = page.getByRole("link", {
            name: "Logout"
        })
    }

    async verifyDashboard(){
        await this.heading.waitFor({ start: "visible"})
    }

    async logout(){
        await this.logoutButton.click()
    }
}
