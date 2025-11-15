<script lang="ts">
export const description = "Teacher disciplinary monitoring page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardTitle,
  CardHeader,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  AlertTriangle,
  ShieldCheck,
  ClipboardCheck,
  Search,
  Plus,
  Eye,
} from "lucide-vue-next"

const userRole = "Teacher"

// Mock incident data
const incidents = ref([
  { id: 1, student: "Carlos Dela Cruz", type: "Bullying", date: "Nov 14, 2025", status: "Pending" },
  { id: 2, student: "Maria Santos", type: "Disruptive Behavior", date: "Nov 12, 2025", status: "Under Review" },
  { id: 3, student: "John Perez", type: "Cheating", date: "Nov 10, 2025", status: "Resolved" },
  { id: 4, student: "Angela Ramos", type: "Uniform Violation", date: "Nov 09, 2025", status: "Pending" },
  { id: 5, student: "Mark Rivera", type: "Classroom Misconduct", date: "Nov 08, 2025", status: "Resolved" },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Disciplinary</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Disciplinary Records</h2>
            <p class="text-sm text-muted-foreground">
              Monitor and manage student behavioral incidents.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Incident
          </Button>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-3">

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Cases Today</CardTitle>
              <AlertTriangle class="h-5 w-5 text-orange-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ incidents.filter(i => i.status === 'Pending').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Active Cases</CardTitle>
              <ClipboardCheck class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ incidents.filter(i => i.status !== 'Resolved').length }}
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Resolved</CardTitle>
              <ShieldCheck class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ incidents.filter(i => i.status === 'Resolved').length }}
              </p>
            </CardContent>
          </Card>

        </div>

        <!-- Incident Table -->
        <Card>
          <CardHeader>
            <CardTitle>Incident Reports</CardTitle>
            <CardDescription>List of all reported student incidents.</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="flex items-center justify-between mb-4">
              <Input v-model="search" placeholder="Search incidents..." class="max-w-xs" />
            </div>

            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Student</TableHead>
                  <TableHead>Type</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="incident in incidents"
                  :key="incident.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell class="font-medium">{{ incident.student }}</TableCell>
                  <TableCell>{{ incident.type }}</TableCell>
                  <TableCell class="text-muted-foreground">{{ incident.date }}</TableCell>

                  <TableCell>
                    <Badge
                      :variant="
                        incident.status === 'Pending'
                          ? 'destructive'
                          : incident.status === 'Under Review'
                          ? 'secondary'
                          : 'default'
                      "
                    >
                      {{ incident.status }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-right">
                    <Button variant="outline" size="sm">
                      <Eye class="h-4 w-4 mr-1" />
                      View
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
