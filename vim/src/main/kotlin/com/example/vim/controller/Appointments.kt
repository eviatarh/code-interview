package com.example.vim.controller

import com.example.vim.model.Appointment
import com.example.vim.service.ProviderService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*
import org.springframework.http.HttpStatus

import org.springframework.http.ResponseEntity
import org.springframework.validation.annotation.Validated


@RestController
@Validated
class Appointments {

    @Autowired
    lateinit var providerService: ProviderService

    @GetMapping("/appointments")
    fun search(
        @RequestParam(value = "specialty", defaultValue = "") specialty: String?,
        @RequestParam(value = "date", defaultValue = "") date: Long?,
        @RequestParam(value = "minScore", defaultValue = "") minScore: Float?
    ) : ResponseEntity<List<String>> {

        return if (specialty.isNullOrEmpty() || date == null || minScore == null ) {
            ResponseEntity(HttpStatus.BAD_REQUEST)
        } else {
            ResponseEntity(providerService.getProviders(specialty, date, minScore), HttpStatus.OK)
        }
    }

    @PostMapping("/appointments")
    fun schedule(@RequestBody appointment: Appointment) : ResponseEntity<Any> {
        return if (providerService.schedule(appointment)) {
            ResponseEntity(null, HttpStatus.OK)
        } else {
            ResponseEntity(null, HttpStatus.BAD_REQUEST)
        }
    }
}