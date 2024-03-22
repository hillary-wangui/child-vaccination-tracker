CREATE TABLE Hospital (
    hospital_id INT AUTO_INCREMENT PRIMARY KEY,
    hospital_name VARCHAR(255),
    location VARCHAR(255),
    contact_info VARCHAR(255)
);

CREATE TABLE MoHBranch (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(255),
    location VARCHAR(255),
    contact_info VARCHAR(255)
);

CREATE TABLE Hospital_MoH_Branches (
    hospital_id INT,
    branch_id INT,
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id),
    FOREIGN KEY (branch_id) REFERENCES MoHBranch(branch_id),
    PRIMARY KEY (hospital_id, branch_id)
);

CREATE TABLE Parent (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    parent_name VARCHAR(255),
    contact_info VARCHAR(255)
);

CREATE TABLE Child (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id INT,
    child_name VARCHAR(255),
    age INT,
    gender VARCHAR(1),
    weight DECIMAL(5,2),
    FOREIGN KEY (parent_id) REFERENCES Parent(parent_id)
);

CREATE TABle VaccinationDetails (
    vaccination_id INT AUTO_INCREMENT PRIMARY KEY,
    child_id INT,
    vaccination_date DATE,
    vaccination_type VARCHAR(255),
    next_vaccination_date DATE,
    FOREIGN KEY (child_id) REFERENCES Child(child_id)
);
