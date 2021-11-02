/*
 * SPDX-License-Identifier: Apache-2.0
 */
/*jshint esversion: 8 */
/* jshint -W097 */
/* jshint node: true */

'use strict';

const { Contract } = require('fabric-contract-api');


class NewGradeContract extends Contract {

    async create_Grade(ctx, staff_id, staff_grade, institution,
        job_role, Staff_name, salary) {
        const exists = await this.Grade_Exists(ctx, staff_id);
        if (exists) {
            throw new Error(`The new grade ${staff_id} already exists`);
        }

        const asset = {
            staff_grade

        };
        const s_institution = {
            institution
        };
        const s_role = {
            job_role
        };
        const s_fname = {
            Staff_name
        };
        const s_salary = { salary };
        const buffer = Buffer.from(JSON.stringify(asset, s_institution, s_role, s_fname, s_salary));
        await ctx.stub.putState(staff_id, buffer);
    }

    async GradeExists(ctx, staff_id) {
        const buffer = await ctx.stub.getState(staff_id);
        return (!!buffer && buffer.length > 0);
    }



    async read_Grade(ctx, staff_id) {
        const exists = await this.newGradeExists(ctx, staff_id);
        if (!exists) {
            throw new Error(`The grade for ${staff_id} does not exist`);
        }
        const buffer = await ctx.stub.getState(staff_id);
        const asset = JSON.parse(buffer.toString());
        return asset;
    }

    async update_Grade(ctx, staff_id, new_staff_grade, new_institution,
        new_job_role, new_Staff_name, new_salary) {
        const exists = await this.newGradeExists(ctx, staff_id);
        if (!exists) {
            throw new Error(`The grade for ${staff_id} does not exis`);
        }
        const asset = {
            staff_grade: new_staff_grade,
            institution: new_institution,
            job_role: new_job_role,
            staff_name: new_Staff_name,
            salary: new_salary
        };
        const buffer = Buffer.from(JSON.stringify(asset));
        await ctx.stub.putState(staff_id, buffer);
    }

    async deleteNewGrade(ctx, staff_id) {
        const exists = await this.newGradeExists(ctx, staff_id);
        if (!exists) {
            throw new Error(`The grade for ${staff_id} does not exist`);
        }
        await ctx.stub.deleteState(staff_id);
    }

}

module.exports = NewGradeContract;
