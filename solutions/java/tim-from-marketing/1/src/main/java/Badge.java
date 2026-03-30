class Badge {
    public String print(Integer id, String name, String department) {
        String finalDepartment;
        if(department == null) {
            finalDepartment = "OWNER"; 
        } else {
            finalDepartment = department.toUpperCase();
        }

        if (id == null) {
          return name + " - " + finalDepartment.toUpperCase();  
        }

        return "[" + id +"] - " + name + " - " + finalDepartment.toUpperCase(); 
}
}